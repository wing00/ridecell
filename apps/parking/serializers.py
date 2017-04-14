from datetime import datetime
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField
from .models import *


class LocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Location
        geo_field = 'point'
        fields = ['id', 'point', 'occupied']


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Reservation
        fields = ['id', 'start_time', 'end_time', 'location']

    def create(self, validated_data):
        location = validated_data.pop('location')

        location_object = Location.objects.create(**location)
        validated_data['location'] = location_object
        reservation = Reservation.objects.create(**validated_data)

        return reservation


class FreeSpotsSerializer(serializers.HyperlinkedModelSerializer):
    queryset = Reservation.objects.all()
    location = LocationSerializer()

    class Meta:
        model = Reservation
        fields = ['id', 'location']


class ReservationsUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'start_time', 'end_time']
