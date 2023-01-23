from django.http import HttpRequest
from django.shortcuts import render

from .models import BankAccount


def index(request: HttpRequest):
    """Homepage"""
    return render(request, "coreApp/index.html")

def bank(request: HttpRequest):
    """The place to view your bank account and it's balance."""
    account: BankAccount = request.user.bankaccount
    balance = account.balance
    context = {"balance": balance}
    return render(request, "coreApp/bank.html", context)
