"""
Application models.
"""
import datetime
import json
import uuid

from django.db import models
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from project.helpers import get_fingerprint


class Manager(models.Manager):
    """
    Applications model manager.
    """
    def fingerprint_map(self):
        """
        Return maping of application fingerprint to application instance.
        """
        results = {}

        for app in self.get_queryset().all():
            results[get_fingerprint(app.timestamp, app.email)] = app

        return results

    def get_unrated(self, user):
        exclude_ids = list(user.rated.values_list("application__id", flat=True))

        queryset = self.get_queryset().exclude(
            id__in=exclude_ids,
        ).exclude(
            Q(approval_level=0)
        ).filter(
            deleted=False,
            rated_count__lt=2,
            duplicate=None,
        ).filter(Q(terminated=False) | Q(approval_level=1) | Q(approval_level=2) | Q(approval_level=3))

        if user.terminator:
            queryset = queryset.filter(approved=False)

        return queryset.order_by("rated_count", "created")

    def get_unrated2(self, user):
        exclude_ids = list(user.rated2.values_list("application__id", flat=True))

        queryset = self.get_queryset().exclude(
            id__in=exclude_ids,
        ).exclude(
            Q(approval_level=0)
        ).filter(
            deleted=False,
            duplicate=None,
            rated2_count__lt=2,
        ).filter((Q(terminated=False) & Q(average_rating__gte=69)) | Q(approval_level=2) | Q(approval_level=3))

        return queryset.order_by("rated2_count", "created")


class Application(models.Model):
    """
    Store application data extrcted from spreadsheet.
    """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    timestamp = models.TextField(blank=False)
    email = models.EmailField(blank=False)
    data = models.TextField(blank=False)
    terminated = models.BooleanField(default=False)
    terminated_by = models.ForeignKey(
        "rating.User",
        null=True,
        related_name="terminated"
    )
    terminated_ip = models.GenericIPAddressField(blank=True, null=True)
    terminated_at = models.DateTimeField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        "rating.User",
        null=True,
        related_name="approved"
    )
    approved_ip = models.GenericIPAddressField(blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    approval_level = models.TextField(blank=True, null=True)
    final_decision = models.TextField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    welcome_sent = models.BooleanField(default=False)
    rated_count = models.IntegerField(default=0)
    rated2_count = models.IntegerField(default=0)
    average_rating = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(editable=False)
    duplicate = models.ForeignKey("self", null=True, blank=True)

    objects = Manager()

    def save(self, *args, **kwargs):
        """
        Add created timestamp.
        """
        if not self.id:
            self.created = datetime.datetime.now()

        super(Application, self).save(*args, **kwargs)

    def welcome(self):
        """
        Send welcome mail to application email address.
        """
        if not settings.WELCOME_MAIL_ENABLED:
            return

        context = {
            "user": self,
        }

        subject = render_to_string(
            "application/email/welcome.subject", context
        ).strip()
        message = render_to_string("application/email/welcome.message", context)
        html_message = render_to_string("application/email/welcome.html-message", context)

        send_mail(
            subject,
            message,
            settings.FROM_MAIL,
            [self.email],
            fail_silently=False,
            html_message=html_message,
        )

        self.welcome_sent = True
        self.save()

    def info(self):
        """
        Returns list of information to show on rate form. Fields are defined in
        settings.APPLICATION_INFO_FIELDS
        """
        info = []
        data = json.loads(self.data)

        for field in settings.APPLICATION_INFO_FIELDS:
            if data.get(field):

                title = field
                if title.endswith("^"):
                    title = field[:-1]

                info.append({
                    "title": title,
                    "content": data[field]
                })

        return info

    def info2(self):
        """
        Returns list of information to show on rate form (PHASE 2).
        Fields are defined in settings.APPLICATION_INFO_FIELDS_PHASE2
        """
        info2 = []
        data = json.loads(self.data)

        for field in settings.APPLICATION_INFO_FIELDS_PHASE2:

            if data.get(field):

                title = field
                if title.endswith("^"):
                    title = field[:-1]

                info2.append({
                    "title": title,
                    "content": data[field]
                })

        return info2

    def get_ratings(self):
        """
        Returns ratings and ratings of duplicates of this application.
        """
        application = self.duplicate or self

        return self.ratings.model.objects.filter(
            models.Q(application=application) | models.Q(application__duplicate=application)
        )

    def get_ratings2(self):
        """
        Returns ratings and ratings of duplicates of this application.
        """
        application = self.duplicate or self

        return self.ratings2.model.objects.filter(
            models.Q(application=application) | models.Q(application__duplicate=application)
        )

    def __repr__(self):
        return str(self.uuid)
