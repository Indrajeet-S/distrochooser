# Generated by Django 4.2.4 on 2023-08-19 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0013_widget_page"),
    ]

    operations = [
        migrations.AlterField(
            model_name="widget",
            name="page",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="widget_page",
                to="web.page",
            ),
        ),
    ]