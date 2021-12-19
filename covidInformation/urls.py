from django.urls import path, include
from .views import *
urlpatterns = [
    path('covid-information', covidCasesInformation, name='covid-information'),
    path('covid-vaccination-center', covidVaccinationInformation, name='covid-vaccination-center')
]