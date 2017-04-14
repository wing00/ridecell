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
    queryset = Location.objects.filter(occupied=False)
    serializer_class = LocationSerializer
    distance_filter_field = 'point'
    filter_backends = (DistanceToPointFilter, )
    filter_fields = ('point', )


class ReservationListView(ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = FreeSpotsSerializer
    distance_filter_field = 'location'
    filter_backends = (DistanceToPointFilter, )
    filter_fields = ('location', )


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationUpdateView(UpdateAPIView):
    queryset = Reservation.objects.filter(location__occupied=False)
    serializer_class = ReservationsUpdateSerializer


