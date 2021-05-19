from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
import api.views as views
from django.urls import path
import api._urls.vehicle_urls as vehicle_urls


router = routers.DefaultRouter()


# router.register(r'vehicles/create', views.CreateVehicleViewSet,basename="create_vehicle")
# # router.register(r'vehicles/create', views.CreateVehicleViewSet)
# router.register(r'vehicles', views.ViewVehiclesListViewSet,basename="view_vehicles")
# router.register(r'vehicles/<str:id>', views.RetrieveVehicleViewSet,basename="retrieve_vehicle")
# router.register(r'vehicles/<str:id>/update', views.UpdateVehicleViewSet,basename="update_vehicle")
# router.register(r'vehicles/<str:id>/delete', views.DeleteVehicleViewSet,basename="delete_vehicle")

urlpatterns = [
    path('', include(router.urls)),
    path(r'vehicles/', include('api._urls.vehicle_urls')),
    # path(r'vehicles/create', views.CreateVehicleViewSet.as_view({'post': 'create'})),
    # path(r'vehicles', views.ViewVehiclesListViewSet.as_view({'get': 'list'})),
    # path(r'vehicles/<str:id>', views.RetrieveVehicleViewSet.as_view({'get': 'retrieve'})),
    # path(r'vehicles/<str:id>/update', views.UpdateVehicleViewSet.as_view({'put': 'update'})),
    # path(r'vehicles/<str:id>/delete', views.DeleteVehicleViewSet.as_view({'destroy': 'destroy'})),
    
]
