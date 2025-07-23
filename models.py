 django.db import models
from django.contrib.auth.models import User

class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30, unique=True)
    level = models.IntegerField(default=1)
    prestige = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname
