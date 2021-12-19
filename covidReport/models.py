from django.db import models
from authentications.models import User
# Create your models here.
class CovidReport(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    report = models.FileField(upload_to='report/')
    isReportPositive = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email