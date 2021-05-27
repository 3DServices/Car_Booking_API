import api._views.directorate as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/',
         views.CreateDirectorateViewSet.as_view({'post': 'create'})),
    path('', views.ViewDirectoratesListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:id>/', views.RetrieveDirectorateViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateDirectorateViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteDirectorateViewSet.as_view({'delete': 'destroy'})),
]
