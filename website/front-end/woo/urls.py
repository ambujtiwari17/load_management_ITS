from django.conf.urls import url
from woo import views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
]