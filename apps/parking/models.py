from django.contrib.gis.db import models
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):
    operations = [
        CreateExtension('postgis'),
    ]


class Locations(models.Model):
    location = models.PointField()


class Reservations(models.Model):
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    occupied = models.BooleanField(default=False)
