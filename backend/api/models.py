from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    bio = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.user.email


class Property(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
