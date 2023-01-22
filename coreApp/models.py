from django.db import models
from django.contrib.auth.models import User

class Balance(models.Model):
    """The money stored in a user's account."""
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return self.amount
