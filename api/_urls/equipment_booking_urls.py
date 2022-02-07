import api._views.equipment_booking_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'', views.ViewEquipmentBookingsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/', views.CreateEquipmentBookingViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveEquipmentBookingViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateEquipmentBookingViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteEquipmentBookingViewSet.as_view({'delete': 'destroy'})),
]
