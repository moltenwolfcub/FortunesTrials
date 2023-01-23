from django.db import models
from django.contrib.auth.models import User

class BankAccount(models.Model):
    """The money stored in a user's account."""
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.balance)+" unnamed currency."
