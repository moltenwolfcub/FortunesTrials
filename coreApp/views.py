from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render
from django.utils import timezone

from .models import BankAccount


def index(request: HttpRequest):
    """Homepage"""
    return render(request, "coreApp/index.html")

@login_required
def bank(request: HttpRequest):
    """The place to view your bank account and it's balance."""
    account: BankAccount = request.user.bankaccount

    balance = account.balance

    sinceDaily: timezone.timedelta = timezone.now()-account.lastDailyReward
    daily: bool = sinceDaily.days >= 1

    context = {"balance": balance, "dailyReady": daily}
    return render(request, "coreApp/bank.html", context)
