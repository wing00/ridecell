from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, UpdateAPIView, ListCreateAPIView, CreateAPIView
from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework.response import Response
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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        loc_instance = instance.location
        loc_instance.occupied = True
        loc_instance.save()

        location = LocationSerializer(loc_instance, data={'occupied': True}, partial=True)
        location.is_valid()
        location.save()
        return Response(serializer.data)

