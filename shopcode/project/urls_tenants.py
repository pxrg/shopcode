from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from shop import urls as shop_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(shop_urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)