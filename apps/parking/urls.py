from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'parkingspot', ParkingSpotListViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^get_spots/lat/(?P<latitude>[\d]+)/long/(?P<longitude>[\d]+)/rad/(?P<radius>[\d]+)/$', ParkingSpotListView.as_view()),
    url(r'^reserve_spot/(?P<parking_spot>[\d]+)/$', ParkingSpotUpdateView.as_view()),
    url(r'^locations/$', LocationListView.as_view()),
]
