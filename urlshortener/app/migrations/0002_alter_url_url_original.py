# Generated by Django 5.1.5 on 2025-01-24 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="url",
            name="url_original",
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
