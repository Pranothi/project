from django.urls import path
from django.contrib import admin
from gesturetest import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.test, name="test")
]