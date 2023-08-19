# Generated by Django 4.2.4 on 2023-08-19 08:33

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Choosable",
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
                ("name", web.models.TranslateableField(max_length=104)),
            ],
        ),
    ]
