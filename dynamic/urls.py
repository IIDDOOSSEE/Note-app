from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("date/", views.show_date, name="datetime"),
    path("directory/", views.show_directoryListing, name="showdirectorylisting"),
]