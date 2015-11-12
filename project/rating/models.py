"""
Rating models.
"""
import datetime
import uuid

from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

from project.helpers import get_fingerprint


class Manager(models.Manager):
    """
    Applications model manager.
    """
    def fingerprint_map(self):
        """
        Return maping of users fingerprint to user instances.
        """
        results = {}

        for user in self.get_queryset().all():
            results[get_fingerprint(user.timestamp, user.email)] = user

        return results


class User(models.Model):
    """
    Users allowed to rate applications.
    """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    timestamp = models.TextField(blank=False)
    email = models.EmailField(blank=False)
    data = models.TextField(blank=False)
    enabled = models.BooleanField(default=False)
    organizer = models.BooleanField(default=False)
    terminator = models.BooleanField(default=False)
    invitation_sent = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    objects = Manager()

    def save(self, *args, **kwargs):
        """
        Add created timestamp.
        """
        if not self.id:
            self.created = datetime.datetime.now()

        super(User, self).save(*args, **kwargs)

    def invite(self):
        """
        Send invite mail to application email address.
        """
        if not settings.REVIEWER_MAIL_ENABLED:
            return

        context = {
            "user": self,
            "link": "{}{}".format(
                settings.BASE_URL,
                reverse("rating:rate", args=[self.uuid])
            )
        }

        subject = render_to_string(
            "rating/email/invite.subject", context
        ).strip()
        message = render_to_string("rating/email/invite.message", context)

        send_mail(
            subject,
            message,
            settings.FROM_MAIL,
            [self.email],
            fail_silently=False
        )
        self.invitation_sent = True
        self.save()


STATE_CHOICES = (
    (True, u'Yes'),
    (False, u'No'),
)


class Step1Rating(models.Model):
    """
    Application rating.
    """
    created_by = models.ForeignKey(User, related_name="rated")
    application = models.ForeignKey("application.Application", related_name="ratings")
    rating = models.IntegerField(blank=False)
    created = models.DateTimeField(editable=False)
    application_incomplete = models.BooleanField(default=False)
    application_unreadable = models.BooleanField(default=False)
    needs_review = models.BooleanField(default=False)
    person_engaged = models.BooleanField(default=False, choices=STATE_CHOICES)
    why_engaged = models.TextField()
    comments = models.TextField()
    conflict = models.BooleanField(default=False)
    ipaddress = models.GenericIPAddressField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Add created timestamp.
        """
        if not self.id:
            self.created = datetime.datetime.now()

        obj = super(Step1Rating, self).save(*args, **kwargs)

        self.application.rated_count += 1
        self.application.average_rating = 0

        ratings = self.application.get_ratings()

        if ratings:
            for rating in ratings:
                self.application.average_rating += rating.rating

            self.application.average_rating = self.application.average_rating / len(ratings)

        self.application.save()

        return obj


class Step2Rating(models.Model):
    """
    Application rating.
    """
    created_by = models.ForeignKey(User, related_name="rated2")
    application = models.ForeignKey("application.Application", related_name="ratings2")
    created = models.DateTimeField(editable=False)
    action = models.IntegerField()
    engagement = models.IntegerField()
    interest = models.IntegerField()
    needs_review = models.BooleanField(default=False)
    application_problem = models.TextField()
    comments = models.TextField(blank=True, null=True)
    ipaddress = models.GenericIPAddressField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Add created timestamp.
        """
        if not self.id:
            self.created = datetime.datetime.now()

        self.application.rated2_count += 1
        self.application.save()

        super(Step2Rating, self).save(*args, **kwargs)

# class Step2Rating -- rate2.html template contains the following:
# {{ forms.rate2.action }}
# {{ forms.rate2.comments }}
# {{ forms.rate2.engagement }}
# {{ forms.rate2.interest }}
# {{ forms.rate2.needs_review }}
# {{ forms.rate2.application_problem }}
