from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import *


class LocationSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Locations
        geo_field = 'point'


class ParkingSpotSerializer(serializers.Serializer):
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    occupied = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Reservations.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.radius = validated_data.get('radius', instance.radius)

        return instance


class ReservationsListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Locations
        fields = ('parking_spot', 'start_time', 'end_time', 'location')


class ReservationsUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Locations
        fields = ('parking_spot', 'start_time', 'end_time', 'occupied')

    def update(self, instance, validated_data):
        instance.parking_spot = validated_data.get('parking_spot', instance.parking_spot)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.occupied = True
        return instance

