# Generated by Django 5.1.1 on 2024-09-14 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BankBook",
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
                ("balance_won", models.IntegerField(default=0)),
                ("balance_dol", models.IntegerField(default=0)),
                ("balance_yen", models.IntegerField(default=0)),
                ("balance_pes", models.IntegerField(default=0)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="main.person"
                    ),
                ),
            ],
        ),
    ]
