from django.urls import path, include
from .views import donation
urlpatterns = [
    path('donation', donation, name='donation')
]