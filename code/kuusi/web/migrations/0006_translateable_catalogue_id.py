# Generated by Django 4.2.4 on 2023-08-19 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0005_translateablefieldrecord_po_block"),
    ]

    operations = [
        migrations.AddField(
            model_name="translateable",
            name="catalogue_id",
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
