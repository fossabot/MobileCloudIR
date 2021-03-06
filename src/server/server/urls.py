from django.conf.urls import url, include
from django.contrib import admin

from server import views

urlpatterns = [
    url(r'^ping/?$', views.ping, name='ping'),
    url(r'^configure/?$', views.configure, name='configure'),
    url(r'^data/?$', views.data_distribute, name='data_distribute'),
    url(r'^multicast_start/?$', views.run_multicast_listener, name='multicast_start'),
    url(r'^query/?$', views.query, name='query'),
    url(r'^test/?$', views.test)
]
