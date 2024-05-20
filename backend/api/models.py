from django.db import models


class Owner(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=40)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Property(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    nearby = models.TextField()
    zip_code = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
