# Generated by Django 4.0.6 on 2022-08-29 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrugGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DrugManufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DrugName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('form', models.TextField(blank=True)),
                ('indications', models.TextField(blank=True)),
                ('more', models.TextField(blank=True)),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='med_app.drugmanufacturer')),
                ('pharmgroup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='med_app.druggroup')),
            ],
        ),
    ]
