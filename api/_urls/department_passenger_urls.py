import api._views.departmentpassenger_views as views
from django.urls import path


urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/',
         views.CreateDepartmentPassengerViewSet.as_view({'post': 'create'})),
    path('', views.ViewAllDepartmentPassengersListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:department_id>/', views.ViewDepartmentPassengersListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:department_id>/<str:id>/', views.RetrieveDepartmentPassengerViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:department_id>/<str:id>/update/',
         views.UpdateDepartmentPassengerViewSet.as_view({'put': 'update'})),
    path(r'<str:department_id>/<str:id>/delete/',
         views.DeleteDepartmentPassengerViewSet.as_view({'delete': 'destroy'})),
]
