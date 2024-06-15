from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Asset(models.Model):
    asset_id = models.CharField(max_length=10)
    asset_name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'[{self.asset_id}-{self.asset_name}]  {self.user}'
