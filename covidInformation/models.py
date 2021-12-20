from django.db import models
from datetime import datetime


class StateName(models.Model):
    stateName = models.CharField(max_length=100, primary_key=True)


class CovidStateCount(models.Model):
    stateName = models.OneToOneField(StateName, on_delete=models.CASCADE, primary_key=True)
    count = models.IntegerField()


class CovidDailyCount(models.Model):
    currentDate = models.DateField(default=datetime.now, blank=True)
    count = models.CharField(max_length=20)


class VaccinationCenters(models.Model):
    stateName = models.ForeignKey(StateName, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=500, blank=False)
    city = models.CharField(max_length=500, blank=False)
