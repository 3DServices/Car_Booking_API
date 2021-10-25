import api._views.department_passengertrip_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/',
         views.CreateDepartmentPassengerTripViewSet.as_view({'post': 'create'})),
    path(r'', views.ViewAllDepartmentPassengerTripsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),

    path(r'<str:passenger_id>/', views.ViewDepartmentPassengerTripsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),

    path(r'<str:passenger_id>/<str:id>/', views.RetrieveDepartmentPassengerTripViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:passenger_id>/<str:id>/update/',
         views.UpdateDepartmentPassengerTripViewSet.as_view({'put': 'update'})),
    path(r'<str:passenger_id>/<str:id>/delete/',
         views.DeleteDepartmentPassengerTripViewSet.as_view({'delete': 'destroy'})),
]
