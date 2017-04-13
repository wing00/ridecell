from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, UpdateAPIView, ListCreateAPIView, CreateAPIView
from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework.mixins import CreateModelMixin
from .serializers import *
from .models import *


class LocationCreateView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationListView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    distance_filter_field = 'point'
    filter_backends = (DistanceToPointFilter, )
    filter_fields = ('point', )


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationUpdateView(UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationsUpdateSerializer


