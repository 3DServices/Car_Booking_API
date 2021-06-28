import api._views.project_vehicle_deploy_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'', views.ViewProjectVehicleDeploysListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/',
         views.CreateProjectVehicleDeployViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveProjectVehicleDeployViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateProjectVehicleDeployViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteProjectVehicleDeployViewSet.as_view({'delete': 'destroy'})),
]
