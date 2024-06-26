# Generated by Django 5.0.6 on 2024-05-20 14:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Owner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("username", models.CharField(max_length=40, unique=True)),
                ("first_name", models.CharField(max_length=40)),
                ("last_name", models.CharField(max_length=40)),
                ("phone_number", models.CharField(max_length=40)),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("last_login", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("address", models.CharField(max_length=40)),
                ("city", models.CharField(max_length=40)),
                ("state", models.CharField(max_length=40)),
                ("nearby", models.TextField()),
                ("zip_code", models.CharField(max_length=40)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.owner"
                    ),
                ),
            ],
        ),
    ]
