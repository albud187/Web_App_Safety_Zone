from django.db import models

# Create your models here.

class FlightSafetyReport(models.Model):

    location = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    time = models.CharField(max_length=4)
    contact = models.CharField(max_lenght=100)
