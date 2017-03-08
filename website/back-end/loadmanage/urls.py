from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^load/',include('load.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', admin.site.urls),
]
