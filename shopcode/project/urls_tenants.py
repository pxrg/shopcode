from django.conf.urls import patterns, url, include
from shop import urls as shop_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(shop_urls)),
)
