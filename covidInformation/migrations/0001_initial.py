# Generated by Django 4.0 on 2021-12-19 12:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CovidDailyCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentDate', models.DateField(blank=True, default=datetime.datetime.now)),
                ('count', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StateName',
            fields=[
                ('stateName', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationCenters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('stateName', models.ManyToManyField(to='covidInformation.StateName')),
            ],
        ),
        migrations.CreateModel(
            name='CovidStateCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(max_length=20)),
                ('stateName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidInformation.statename', unique=True)),
            ],
        ),
    ]