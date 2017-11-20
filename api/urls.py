"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ListCVs, CVbyRegionText

urlpatterns = [
    url(r'^simplecv/$', ListCVs.as_view(), name='list-cv'),
    url(r'^simplecv/(?P<regionId>[0-9]+)/$', CVbyRegionText.as_view(), name='region-CV'),
    url(r'^simplecv/(?P<regionId>[0-9]+)/(?P<text>.+)/$', CVbyRegionText.as_view(), name='region-CV-filtered'),
    url(r'^simplecv/(?P<text>.+)/$', CVbyRegionText.as_view(), name='text-CV'),
    ]