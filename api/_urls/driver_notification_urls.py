import api._views.driver_notitification_views as views
from django.urls import path


urlpatterns = [
    # path('', include(router.urls)),
    path(r'', views.ViewDriverNotificationsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/',
         views.CreateDriverNotificationViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveDriverNotificationViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateDriverNotificationViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteDriverNotificationViewSet.as_view({'delete': 'destroy'})),
]
