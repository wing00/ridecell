from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework.mixins import CreateModelMixin
from .serializers import *
from .models import *


class LocationListView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    distance_filter_field = 'point'
    filter_backends = (DistanceToPointFilter, )
    filter_fields = ('point', )


class ParkingSpotListViewSet(ModelViewSet):
    queryset = Reservations.objects.all()
    serializer_class = ParkingSpotSerializer


class ParkingSpotListView(ListAPIView):
    serializer_class = ReservationsListSerializer
    lookup_field = ('latitude')

    def get_queryset(self):
        return Reservations.objects.filter(occupied=False)


class ParkingSpotUpdateView(UpdateAPIView):
    serializer_class = ReservationsUpdateSerializer
    lookup_field = ('parking_spot')




