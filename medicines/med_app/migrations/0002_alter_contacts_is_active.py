# Generated by Django 4.0.6 on 2023-01-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]