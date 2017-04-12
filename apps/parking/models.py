from django.db import models


class ParkingSpots(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.FloatField()
    parking_spot = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

