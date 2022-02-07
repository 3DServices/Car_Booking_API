import api._views.equipment_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
   # path('', include(router.urls)),
    path(r'', views.ViewEquipmentsListViewSet.as_view({'get': 'list'}),name="view_vehicles"),
    path(r'create/', views.CreateEquipmentViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveEquipmentViewSet.as_view({'get': 'retrieve'}),name="retrieve_vehicle"),
    path(r'<str:id>/update/', views.UpdateEquipmentViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/', views.DeleteEquipmentViewSet.as_view({'delete': 'destroy'})),    
]
