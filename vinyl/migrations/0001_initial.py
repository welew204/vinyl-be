# Generated by Django 4.2.9 on 2024-01-20 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Album",
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
                ("title", models.CharField(max_length=120)),
                ("artist", models.CharField(max_length=120)),
                ("bringer", models.CharField(max_length=120)),
            ],
        ),
    ]