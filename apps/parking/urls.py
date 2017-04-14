from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *
"""
Using django-filters & django-rest-gis

private location endpoint
/add_location/

public location endpoint
/location/?dist=<radius>&point=<long>,<lat>
/location/?dist=1&point=10,10



curl -XPATCH -H "Content-type: application/json" -d '{"start_time":"2018-04-12T01:01:00Z", "occupied":true}' http://localhost:8000/reserve_spot/11/


"""

router = DefaultRouter()
router.register(r'parking_spot', ReservationViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^add_location/$', LocationCreateView.as_view()),
    url(r'^location/$', LocationListView.as_view()),
    url(r'^free_spot/$', ReservationListView.as_view()),
    url(r'^reserve_spot/(?P<pk>[\d]+)/$', ReservationUpdateView.as_view()),
]
