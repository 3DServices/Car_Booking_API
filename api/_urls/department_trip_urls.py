import api._views.department_trip_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'', views.ViewDepartmentTripsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/',
         views.CreateDepartmentTripViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveDepartmentTripViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateDepartmentTripViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteDepartmentTripViewSet.as_view({'delete': 'destroy'})),
]
