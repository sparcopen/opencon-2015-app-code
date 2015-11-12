"""
Application urlconfig
"""
from __future__ import absolute_import

from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r"^(?P<uuid>[0-9a-f-]{36})/$",
        views.RateView.as_view(),
        name="rate"
    ),
    url(
        r"^2/(?P<uuid>[0-9a-f-]{36})/$",
        views.Rate2View.as_view(),
        name="rate2"
    )
]
