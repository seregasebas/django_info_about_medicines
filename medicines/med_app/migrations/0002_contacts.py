# Generated by Django 4.0.6 on 2022-10-02 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('email', models.EmailField(max_length=64, unique=True)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]