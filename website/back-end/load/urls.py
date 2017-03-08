from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^complaint/$',views.complain,name='complaint'),
    url(r'^appliance/$',views.appliance,name='appliance'),
    url(r'^use/$',views.use,name='usage'),
    url(r'^(?P<appliance_id>[0-9]+)/$',views.details,name='details'),
]
