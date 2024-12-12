from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("note.urls")),
    path("note/", include("note.urls")),
    path("dynamic/", include("dynamic.urls")),
    path("admin/", admin.site.urls)
    
]