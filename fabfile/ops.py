"""
Unity playground scripts.
"""
import json

from fabric.api import task
from django.conf import settings

from application.models import Application
from project.helpers import get_fingerprint
from rating.models import User
from spreadsheet.models import Token, Sheet


def authorize_token(token):
    """
    Store access/refresh token.
    """
    gdata_token = token.initialize()
    url = gdata_token.generate_authorize_url(
        redirect_uri='urn:ietf:wg:oauth:2.0:oob'
    )

    print url

    code = raw_input("Enter code:")

    response = gdata_token.get_access_token(code)
    token.access_token = response.access_token
    token.refresh_token = response.refresh_token
    token.save()


def get_token():
    """
    Get or create token.
    """
    try:
        token = Token.objects.get(name=settings.TOKEN_NAME)
    except Token.DoesNotExist:
        client_id = raw_input("Client id:")
        client_secret = raw_input("Client secret:")
        token = Token.objects.create(
            name=settings.TOKEN_NAME,
            scope=settings.TOKEN_SCOPE,
            client_id=client_id,
            client_secret=client_secret
        )

    if not (token.access_token and token.refresh_token):
        authorize_token(token)

    return token


def get_sheet(name):
    """
    Get or create sheet record.
    """
    try:
        sheet = Sheet.objects.get(name=settings.SHEET_NAMES[name])
    except Sheet.DoesNotExist:
        key = raw_input("Enter {} spreadsheet key:".format(name))

        sheet = Sheet.objects.create(
            name=settings.SHEET_NAMES[name],
            token=get_token(),
            key=key
        )

    return sheet


@task
def initialize():
    """
    Initialize sheet and token.
    """
    get_token()
    get_sheet("applications")
    get_sheet("users")


def update_users():
    new_data = []
    local_data = User.objects.fingerprint_map()
    fresh_data = get_sheet("users").get_data()
    fields = settings.USER_FIELDS

    for item in fresh_data:

        fingerprint = get_fingerprint(
            item[fields["timestamp"]],
            item[fields["email"]],
        )

        try:
            local_item = local_data.pop(fingerprint)
            local_item.data = json.dumps(item)
            local_item.enabled = item.get(fields["enabled"]) == "TRUE"
            local_item.organizer = item.get(fields["organizer"]) == "TRUE"
            local_item.terminator = item.get(fields["terminator"]) == "TRUE"
            local_item.save()
        except KeyError:
            new_data.append(
                User.objects.create(
                    timestamp=item[fields["timestamp"]],
                    email=item[fields["email"]],
                    data=json.dumps(item),
                    enabled=item.get(fields["enabled"]) == "TRUE",
                    organizer=item.get(fields["organizer"]) == "TRUE",
                    terminator=item.get(fields["terminator"]) == "TRUE",
                )
            )

    for deleted_item in local_data.values():
        deleted_item.deleted = True
        deleted_item.save()

    for user in User.objects.filter(deleted=False, enabled=True, invitation_sent=False):
        user.invite()


def update_applications():
    new_data = []
    email_map = {}
    updatad_emails = []

    for email, _id in Application.objects.values_list("email", "id"):

        if email in email_map:
            if _id < email_map[email]:
                email_map[email] = _id
        else:
            email_map[email] = _id

    fresh_data = get_sheet("applications").get_data()
    fields = settings.APPLICATION_FIELDS

    for item in fresh_data:
        email = item[fields["email"]]

        if email in email_map:

            if email not in updatad_emails:
                print "Update application: {}".format(email)
                application = Application.objects.get(pk=email_map[email])
                application.data = json.dumps(item)
                application.approval_level = item[fields["approval_level"]]
                application.final_decision = item[fields["final_decision"]]
                application.save()
                updatad_emails.append(email)
            else:
                continue

        else:
            print "Create application: {}".format(email)
            application = Application.objects.create(
                timestamp=item[fields["timestamp"]],
                email=item[fields["email"]],
                data=json.dumps(item),
                approval_level=item[fields["approval_level"]],
                final_decision=item[fields["final_decision"]]

            )
            new_data.append(application)

            email_map[email] = application.id
            updatad_emails.append(email)

    # for application in Application.objects.filter(deleted=False, welcome_sent=False):
    #     application.welcome()


@task
def update():
    """
    Update local data from spreadsheet.
    """
    udpate_users()
    update_applications()
