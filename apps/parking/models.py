from django.contrib.gis.db import models
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):
    operations = [
        CreateExtension('postgis'),
    ]


class Location(models.Model):
    point = models.PointField()


class Reservations(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    occupied = models.BooleanField(default=False)
