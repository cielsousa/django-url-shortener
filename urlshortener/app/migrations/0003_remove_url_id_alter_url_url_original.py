# Generated by Django 5.1.5 on 2025-01-24 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_url_url_original"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="url",
            name="id",
        ),
        migrations.AlterField(
            model_name="url",
            name="url_original",
            field=models.CharField(max_length=256, primary_key=True, serialize=False),
        ),
    ]
