################### Imports ##################
from django.conf.urls import url
from . import views
import django.contrib.auth.views as auth_views
from django.contrib.auth.decorators import login_required

##################### Source ####################
#----------------------------------------------------------------------------------------
urlpatterns = [
    #-----------------------------------------------------------------
    # Basic index page for the application
    url(r'^$', views.index , name='index'),
    url(r'^index.html$', views.indexnew , name='index'),
    url(r'^login.html$', views.login_user , name='login_user'),
    #url(r'^register.html$', views.register , name='register'),
    #url(r'^logout.html$', views.logout_user , name='logout_user'),'''
    
    
    
    # Page to register a new user
]
