import authentication._views.driver as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/',
         views.CreateDriverViewSet.as_view({'post': 'create'})),
    path('', views.ViewDriversListViewSet.as_view(
        {'get': 'list'}), name="view_driver"),
    path(r'<str:id>/', views.RetrieveDriverViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_driver"),
    path(r'<str:id>/update/',
         views.UpdateDriverViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteDriverViewSet.as_view({'delete': 'destroy'})),
]
