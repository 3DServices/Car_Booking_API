import api._views.department as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/',
         views.CreateDepartmentViewSet.as_view({'post': 'create'})),
    path('', views.ViewDepartmentsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:id>/', views.RetrieveDepartmentViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateDepartmentViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteDepartmentViewSet.as_view({'delete': 'destroy'})),
]
