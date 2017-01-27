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
    url(r'^pages/index.html$', views.indexnew , name='index'),
    # Page to register a new user
]
