"""
Repair scripts.
"""

from fabric.api import task

from application.models import Application


@task
def duplicates():
    """
    Fix application duplicates.
    """
    emails = set(Application.objects.values_list("email", flat=True))

    print len(emails)

    for email in emails:
        applications = Application.objects.filter(email=email)

        original = applications[0]

        for application in applications[1:]:
            application.duplicate = original
            application.save()
        print email


@task
def ratings():
    """
    Calculate average ratings.
    """
    applications = Application.objects.filter(
        terminated=False,
        deleted=False,
        duplicate=None,
    )

    for application in applications:
        ratings = application.get_ratings()
        application.average_rating = 0
        application.rated2_count = len(application.get_ratings2())

        if ratings:
            for rating in ratings:
                application.average_rating += rating.rating

            application.average_rating = application.average_rating / len(ratings)

        application.save()
