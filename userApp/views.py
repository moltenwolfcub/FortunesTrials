from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.shortcuts import redirect, render


def register(request: HttpRequest):
    """Create a new user account"""
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("fortunes_trials:index")

    context = {"form": form}
    return render(request, "registration/register.html", context)
