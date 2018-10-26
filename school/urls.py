from django.conf.urls import url
from django.contrib import admin

from school import views

urlpatterns = [
    url(r'^$', views.index),
]
