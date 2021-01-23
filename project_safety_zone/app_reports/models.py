from django.db import models

# Create your models here.

class FlightSafetyReport(models.Model):
    location = models.CharField(max_length=100)
    description = models.TextField()
    date_time = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)
