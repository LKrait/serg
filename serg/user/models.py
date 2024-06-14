from django.db import models
from django.utils import timezone


class Account(models.Model):
    account_id = models.CharField(max_length=20)
    account_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"[ Customer-{self.account_id} ] : {self.account_name}"
