from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from bot import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^search/(?P<puid>\w+),(?P<type>\d+)/$', views.search, name='search')
]
