
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
import authentication.views as views
from django.urls import path
import authentication._urls.driver as driver_urls
import authentication._urls.passenger as passenger_urls
import authentication._urls.system_admin as system_admin_urls
import authentication._urls.fleet_manager as fleet_manager_urls

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'drivers/', include(driver_urls)),
    path(r'passengers/', include(passenger_urls)),
    path(r'systemadmins/', include(system_admin_urls)),
    path(r'fleetmanagers/', include(fleet_manager_urls)),
]
