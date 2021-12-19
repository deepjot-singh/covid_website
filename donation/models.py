from django.db import models
from authentications.models import User
from datetime import datetime
# Create your models here.
class DonationTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
    card_no = models.CharField(max_length=100)
    transaction_date = models.DateField(default=datetime.now, blank=True)