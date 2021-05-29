from django.conf.urls import include
from django.urls import path
from rest_framework import routers
import api._urls.vehicle_urls as vehicle_urls
import api._urls.organisation as organisation_urls
import api._urls.organisation_fleet_manager as organisation_fleet_manager_urls
import api._urls.organisation_driver as organisation_driver_urls
import api._urls.organisation_vehicle as organisation_vehicle_urls
import api._urls.project as project_urls
import api._urls.branch as branch_urls
import api._urls.station as station_urls
import api._urls.department as department_urls
import api._urls.directorate as directorate_urls
import api._urls.blacklist as blacklist_urls
import api._urls.passenger_blacklist as passenger_blacklist_urls
import api._urls.driver_blacklist as driver_blacklist_urls
import api._urls.vehicle_blacklist as vehicle_blacklist_urls

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(r'vehicles/', include(vehicle_urls)),
    path(r'blacklists/', include(blacklist_urls)),
    path(r'branches/', include(branch_urls)),
    path(r'departments/', include(department_urls)),
    path(r'directorates/', include(directorate_urls)),
    path(r'driverblacklists/', include(driver_blacklist_urls)),
    path(r'organisationdrivers/', include(organisation_driver_urls)),
    path(r'organisationfleetmanagers/',
         include(organisation_fleet_manager_urls)),
    path(r'organisationvehicles/', include(organisation_vehicle_urls)),
    path(r'organisations/', include(organisation_urls)),
    path(r'passengerblacklists/', include(passenger_blacklist_urls)),
    path(r'projects/', include(project_urls)),
    path(r'stations/', include(station_urls)),
    path(r'vehicleblacklists/', include(vehicle_blacklist_urls)),
]
