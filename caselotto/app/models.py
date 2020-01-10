from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    owner = models.OneToOneField('Profile', on_delete=models.CASCADE)
    lotto_points = models.FloatField()

class Case(models.Model):
    owner = models.ForeignKey('Profile', on_delete=models.CASCADE)
    opened = models.BooleanField(default=False)


class Profile(models.Model):
    profile_picture = models.URLField()
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.username