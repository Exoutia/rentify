# Generated by Django 5.0.6 on 2024-05-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_remove_userprofile_date_joined_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="bio",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
