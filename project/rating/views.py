"""
Application view.
"""
from datetime import datetime
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View

from application.models import Application

from .forms import Step1RateForm, Step2RateForm, TerminateForm, ApproveForm
from .models import User


class RateView(View):
    """
    Find user by uuid and allow to rate other applications.
    Do not allow to vote multiple times for same application.
    Constraints for normal application:
        - show only application with less than 2 votes
        - sort application by vote count and created
    Constraints for terminator application:
        - show all applications
        - sort application by vote count and created
    """

    def get_context_data(self, created_by, application, rate_form=None):
        if not rate_form:
            rate_form = Step1RateForm(
                initial={
                    "created_by": created_by.id,
                    "application": application.id,
                }
            )

        context = {
            "user": created_by,
            "rate_count": created_by.rated.count(),
            "application": application.info,
            "forms": {
                "rate": rate_form,
                "terminate": TerminateForm(
                    initial={
                        "terminate": True,
                        "application": application.uuid
                    }
                ),
                "approve": ApproveForm(
                    initial={
                        "approve": True,
                        "application": application.uuid
                    }
                ),
            }
        }

        return context

    def get(self, request, uuid=None):
        try:
            created_by = User.objects.get(uuid=uuid)
        except User.DoesNotExist:
            raise Http404

        unrated = Application.objects.get_unrated(created_by)

        if unrated:
            if created_by.terminator:
                request.session["last_application"] = str(unrated[0].uuid)

            template_name = "rating/rate.html"
            context = self.get_context_data(created_by, unrated[0])

        else:
            template_name = "rating/all_rated.html"
            context = {"user": created_by}

        return render(request, template_name, context=context)

    def rate(self, request, uuid):
        """
        Save rating and redirect to rate view.
        """
        rate_form = Step1RateForm(request.POST)

        if rate_form.is_valid():
            rating = rate_form.save(commit=False)

            if str(rating.created_by.uuid) == uuid:
                rating.ipaddress = (
                    request.META.get("HTTP_X_REAL_IP") or request.META["REMOTE_ADDR"]
                )
                rating.save()
        else:

            try:
                created_by = User.objects.get(uuid=uuid)
            except User.DoesNotExist:
                raise Http404

            application = rate_form.cleaned_data["application"]

            context = self.get_context_data(
                created_by, application, rate_form=rate_form
            )
            template_name = "rating/rate.html"

            return render(request, template_name, context=context)

        return redirect("rating:rate", uuid)

    def terminate(self, request, uuid):
        """
        Terminate application.
        """
        try:
            user = User.objects.get(uuid=uuid)
        except User.DoesNotExist:
            raise Http404

        try:
            application = Application.objects.get(
                uuid=request.session.get("last_application")
            )

            if str(application.uuid) != request.POST["application"]:
                return redirect("rating:rate", uuid)

        except Application.DoesNotExist:
            raise Http404

        if user.terminator:
            application.terminated = True
            application.terminated_by = user
            application.terminated_ip = (
                request.META.get("HTTP_X_REAL_IP") or request.META["REMOTE_ADDR"]
            )
            application.terminated_at = datetime.now()
            application.save()

        return redirect("rating:rate", uuid)

    def approve(self, request, uuid):
        """
        Approve application.
        """
        try:
            user = User.objects.get(uuid=uuid)
        except User.DoesNotExist:
            raise Http404

        try:
            application = Application.objects.get(
                uuid=request.session.get("last_application")
            )

            if str(application.uuid) != request.POST["application"]:
                return redirect("rating:rate", uuid)

        except Application.DoesNotExist:
            raise Http404

        if user.terminator:
            application.approved = True
            application.approved_by = user
            application.approved_ip = (
                request.META.get("HTTP_X_REAL_IP") or request.META["REMOTE_ADDR"]
            )
            application.approved_at = datetime.now()
            application.save()

        return redirect("rating:rate", uuid)

    def post(self, request, uuid=None):
        """
        Handle terminate or rate request.
        """
        if request.POST.get("terminate"):
            return self.terminate(request, uuid)
        elif request.POST.get("approve"):
            return self.approve(request, uuid)
        else:
            return self.rate(request, uuid)


class Rate2View(View):
    """
    Find user by uuid and allow to rate applications.
    """

    def get_context_data(self, created_by, application, rate_form=None):
        if not rate_form:
            rate_form = Step2RateForm(
                initial={
                    "created_by": created_by.id,
                    "application": application.id,
                }
            )

        context = {
            "user": created_by,
            "rate_count": created_by.rated2.count(),
            "application": application.info2(),
            "average_rating": application.average_rating,
            "approval_level": application.approval_level,
            "forms": {
                "rate": rate_form,
            }
        }

        return context

    def get(self, request, uuid=None):
        try:
            created_by = User.objects.get(uuid=uuid)
        except User.DoesNotExist:
            raise Http404

        unrated = Application.objects.get_unrated2(created_by)

        if unrated:
            template_name = "rating/rate2.html"
            context = self.get_context_data(created_by, unrated[0])
        else:
            template_name = "rating/all_rated.html"
            context = {"user": created_by}

        return render(request, template_name, context=context)

    def rate(self, request, uuid):
        """
        Save rating and redirect to rate view.
        """
        rate_form = Step2RateForm(request.POST)

        if rate_form.is_valid():
            rating = rate_form.save(commit=False)

            if str(rating.created_by.uuid) == uuid:
                rating.ipaddress = (
                    request.META.get("HTTP_X_REAL_IP") or request.META["REMOTE_ADDR"]
                )
                rating.save()
        else:

            try:
                created_by = User.objects.get(uuid=uuid)
            except User.DoesNotExist:
                raise Http404

            application = rate_form.cleaned_data["application"]

            context = self.get_context_data(
                created_by, application, rate_form=rate_form
            )
            template_name = "rating/rate2.html"

            return render(request, template_name, context=context)

        return redirect("rating:rate2", uuid)

    def post(self, request, uuid=None):
        """
        Handle terminate or rate request.
        """
        return self.rate(request, uuid)
