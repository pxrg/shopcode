from django.conf.urls import patterns, url

from core.views import RegisterClientView

urlpatterns = patterns(
    '',
    url(r'^$', RegisterClientView.as_view(), name='register'),
)
