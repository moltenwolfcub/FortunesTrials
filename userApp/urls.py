from django.urls import include, path

from coreApp import views

app_name = "users"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
]
