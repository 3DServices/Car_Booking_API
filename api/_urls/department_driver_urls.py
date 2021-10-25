import api._views.department_driver_views as views
from django.urls import path


urlpatterns = [
    path(r'create/',
         views.CreateDepartmentDriverViewSet.as_view({'post': 'create'})),
    path('<str:department_id>/', views.ViewDepartmentDriversListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:department_id>/<str:id>/', views.RetrieveDepartmentDriverViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:department_id>/<str:id>/update/',
         views.UpdateDepartmentDriverViewSet.as_view({'put': 'update'})),
    path(r'<str:department_id>/<str:id>/delete/',
         views.DeleteDepartmentDriverViewSet.as_view({'delete': 'destroy'})),
]
