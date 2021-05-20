from django.conf.urls import include
from django.urls import path
from rest_framework import routers
import api._urls.vehicle_urls as vehicle_urls


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(r'vehicles/', include(vehicle_urls)),
]
