import api._views.department_vehicle_views as views
from django.urls import path


urlpatterns = [
    path(r'create/',
         views.CreateDepartmentVehicleViewSet.as_view({'post': 'create'})),
    path('<str:department_id>/', views.ViewDepartmentVehiclesListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:department_id>/<str:id>/', views.RetrieveDepartmentVehicleViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:department_id>/<str:id>/update/',
         views.UpdateDepartmentVehicleViewSet.as_view({'put': 'update'})),
    path(r'<str:department_id>/<str:id>/delete/',
         views.DeleteDepartmentVehicleViewSet.as_view({'delete': 'destroy'})),
]
