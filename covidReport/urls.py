from django.urls import path, include
from .views import *
urlpatterns = [
    path('upload-report', uploadReport, name='upload-report'),
    path('status-report', statusReport, name='status-report')
]