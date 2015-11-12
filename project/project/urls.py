"""
OpenCon main url configuration.
"""
from django.conf.urls import include, url


urlpatterns = [
    url(r'^rate/', include("rating.urls", namespace="rating")),
]
