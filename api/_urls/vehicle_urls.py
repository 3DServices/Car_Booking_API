from django.conf.urls import url, include
from rest_framework import routers
import api.views as views
from django.urls import path


router = routers.DefaultRouter()
# router.register(r'vehicles/create', views.CreateVehicleViewSet,basename="create_vehicle")
# # router.register(r'vehicles/create', views.CreateVehicleViewSet)
# router.register(r'vehicles', views.ViewVehiclesListViewSet,basename="view_vehicles")
# router.register(r'vehicles/<str:id>', views.RetrieveVehicleViewSet,basename="retrieve_vehicle")
# router.register(r'vehicles/<str:id>/update', views.UpdateVehicleViewSet,basename="update_vehicle")
# router.register(r'vehicles/<str:id>/delete', views.DeleteVehicleViewSet,basename="delete_vehicle")

urlpatterns = [
   # path('', include(router.urls)),
    path(r'create/', views.CreateVehicleViewSet.as_view({'post': 'create'})),
    path('', views.ViewVehiclesListViewSet.as_view({'get': 'list'}),name="view_vehicles"),
    path(r'<str:id>/', views.RetrieveVehicleViewSet.as_view({'get': 'retrieve'}),name="retrieve_vehicle"),
    path(r'<str:id>/update/', views.UpdateVehicleViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/', views.DeleteVehicleViewSet.as_view({'destroy': 'destroy'})),
    
]
