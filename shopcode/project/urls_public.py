from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    '',
    url(r'^', include('core.urls', namespace='core')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
