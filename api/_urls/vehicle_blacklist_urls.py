import api._views.vehicle_blacklist_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/',
         views.CreateVehicleBlacklistViewSet.as_view({'post': 'create'})),
    path('', views.ViewVehicleBlacklistsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:id>/', views.RetrieveVehicleBlacklistViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateVehicleBlacklistViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteVehicleBlacklistViewSet.as_view({'delete': 'destroy'})),
]
