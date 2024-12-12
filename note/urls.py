from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:note_id>/", views.detail, name="detail"),
    path("add/", views.add_note, name="add_note")
]