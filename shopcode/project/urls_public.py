from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    '',
    url(r'^', include('core.urls', namespace='public')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
