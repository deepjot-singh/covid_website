from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([StateName, CovidStateCount, CovidDailyCount, VaccinationCenters])