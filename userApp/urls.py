from django.urls import include, path

from userApp import views

app_name = "users"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
]
