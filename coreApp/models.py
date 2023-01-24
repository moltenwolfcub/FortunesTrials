from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BankAccount(models.Model):
    """The money stored in a user's account."""
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    
    lastDailyReward = models.DateTimeField(default=timezone.now()-timezone.timedelta(days=1))

    def __str__(self) -> str:
        return str(self.balance)+" unnamed currency."
