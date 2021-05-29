import authentication._views.fleet_manager as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/',
         views.CreateFleetManagerViewSet.as_view({'post': 'create'})),
    path('', views.ViewFleetManagersListViewSet.as_view(
        {'get': 'list'}), name="view_fleet_manager"),
    path(r'<str:id>/', views.RetrieveFleetManagerViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_fleet_manager"),
    path(r'<str:id>/update/',
         views.UpdateFleetManagerViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteFleetManagerViewSet.as_view({'delete': 'destroy'})),
]
