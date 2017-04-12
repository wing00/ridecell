from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


class ParkingSpotViewSet(ModelViewSet):
    queryset = ParkingSpots.objects.all()
    serializer_class = ParkingSpotSerializer

