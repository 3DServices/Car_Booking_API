import api._views.driver_blacklist_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/',
         views.CreateDriverBlacklistViewSet.as_view({'post': 'create'})),
    path('', views.ViewDriverBlacklistsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:id>/', views.RetrieveDriverBlacklistViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    # path(r'<str:id>/update/',
    #      views.UpdateDriverBlacklistViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteDriverBlacklistViewSet.as_view({'delete': 'destroy'})),
]
