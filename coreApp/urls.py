from django.urls import path

from coreApp import views

app_name = "fortunes_trials"
urlpatterns = [
    path("", views.index, name="index"),
    path("bankAccount/", views.bank, name="bank"),
]
