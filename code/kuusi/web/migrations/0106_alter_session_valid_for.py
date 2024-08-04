# Generated by Django 4.2.4 on 2024-05-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0105_remove_page_require_session"),
    ]

    operations = [
        migrations.AlterField(
            model_name="session",
            name="valid_for",
            field=models.CharField(
                blank=True, default="latest", max_length=15, null=True
            ),
        ),
    ]