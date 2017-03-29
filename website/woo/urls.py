from django.conf.urls import url
from woo import views
from .views import *
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

urlpatterns = [
    url(r'^$', auth_views.login, {'template_name' : 'login.html'}, name='login'),
    url(r'^dashboard/$', views.HomePageView, name='index'),
    url(r'^sel/$',views.sel, name='sel'),
    url(r'^complaint/$',views.complain,name='complaint'),
    #url(r'^appliance/$',views.appliance,name='appliance'),
    #url(r'^use/$',views.use,name='usage'),
    url(r'^(?P<appliance_id>[0-9]+)/$',views.details,name='details'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/load/'}, name='logout'),
    url(r'^add/(?P<aid>[0-9]+)/(?P<value>[0-9]+)/$',views.adddata)
]