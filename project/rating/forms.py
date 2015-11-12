"""
Application forms.
"""
from django import forms

from application.models import Application

from .models import User, Step1Rating, Step2Rating


class Step1RateForm(forms.ModelForm):
    """
    Rate application.
    """
    created_by = forms.CharField(widget=forms.HiddenInput)
    application = forms.CharField(widget=forms.HiddenInput)
    rating = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    application_incomplete = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    application_unreadable = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    needs_review = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    person_engaged = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    why_engaged = forms.CharField(widget=forms.Textarea, required=False)
    comments = forms.CharField(widget=forms.Textarea, required=False)
    conflict = forms.BooleanField(widget=forms.CheckboxInput, required=False)

    class Meta:
        model = Step1Rating
        fields = [
            "created_by", "application", "rating",
            "application_incomplete", "application_unreadable", "needs_review",
            "person_engaged", "why_engaged", "comments", "conflict"
        ]

    def clean_rating(self):
        try:
            rating = int(self.cleaned_data["rating"])
        except ValueError:
            rating = -1

        if rating < 1 or rating > 100:
            raise forms.ValidationError("Please enter value between 0 and 10.")

        return rating

    def clean_created_by(self):
        try:
            return User.objects.get(
                pk=self.cleaned_data["created_by"]
            )
        except User.DoesNotExist:
            raise forms.ValidationError()

    def clean_application(self):
        try:
            return Application.objects.get(
                pk=self.cleaned_data["application"]
            )
        except Application.DoesNotExist:
            raise forms.ValidationError()


class Step2RateForm(forms.ModelForm):
    """
    Step 2 form.
    """
    class Meta:
        model = Step2Rating
        fields = [
            "created_by", "application", "action",
            "engagement", "interest", "needs_review",
            "application_problem", "comments"
        ]

    created_by = forms.CharField(widget=forms.HiddenInput)
    application = forms.CharField(widget=forms.HiddenInput)
    action = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    comments = forms.CharField(widget=forms.Textarea, required=False)
    engagement = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    interest = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    needs_review = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    application_problem = forms.CharField(widget=forms.Textarea, required=False)

    def clean_created_by(self):
        try:
            return User.objects.get(
                pk=self.cleaned_data["created_by"]
            )
        except User.DoesNotExist:
            raise forms.ValidationError()

    def clean_application(self):
        try:
            return Application.objects.get(
                pk=self.cleaned_data["application"]
            )
        except Application.DoesNotExist:
            raise forms.ValidationError()


class TerminateForm(forms.Form):
    terminate = forms.BooleanField(widget=forms.HiddenInput)
    application = forms.CharField(widget=forms.HiddenInput)


class ApproveForm(forms.Form):
    approve = forms.BooleanField(widget=forms.HiddenInput)
    application = forms.CharField(widget=forms.HiddenInput)
