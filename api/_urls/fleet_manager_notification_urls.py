import api._views.fleet_manager_notitification_views as views
from django.urls import path


urlpatterns = [
    # path('', include(router.urls)),
    path(r'', views.ViewFleetManagerNotificationsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/',
         views.CreateFleetManagerNotificationViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveFleetManagerNotificationViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateFleetManagerNotificationViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteFleetManagerNotificationViewSet.as_view({'delete': 'destroy'})),
]
