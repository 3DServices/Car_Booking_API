import api._views.station_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/', views.CreateStationViewSet.as_view({'post': 'create'})),
    path('', views.ViewStationsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:id>/', views.RetrieveStationViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateStationViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteStationViewSet.as_view({'delete': 'destroy'})),
]
