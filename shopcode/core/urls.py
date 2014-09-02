from django.conf.urls import patterns, url

from django.views.generic.base import TemplateView
from core.views import RegisterClientView

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(
        template_name='index.html'), name='home'),
    url(r'^register/$', RegisterClientView.as_view(), name='register'),
)
