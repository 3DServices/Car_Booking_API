import authentication._views.passenger as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/',
         views.CreatePassengerViewSet.as_view({'post': 'create'})),
    path('', views.ViewPassengersListViewSet.as_view(
        {'get': 'list'}), name="view_passenger"),
    path(r'<str:id>/', views.RetrievePassengerViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_passenger"),
    path(r'<str:id>/update/',
         views.UpdatePassengerViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeletePassengerViewSet.as_view({'delete': 'destroy'})),
]
