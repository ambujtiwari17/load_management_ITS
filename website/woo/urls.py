from django.conf.urls import url
from woo import views
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^load/sel/$',views.sel, name='sel'),
    url(r'^load/complaint/$',views.complain,name='complaint'),
    url(r'^load/appliance/$',views.appliance,name='appliance'),
    url(r'^load/use/$',views.use,name='usage'),
    url(r'^load/(?P<appliance_id>[0-9]+)/$',views.details,name='details'),
]