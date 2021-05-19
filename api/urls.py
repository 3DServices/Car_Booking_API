from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
import api.views as views
from django.urls import path


router = routers.DefaultRouter()
router.register(r'vehicles/create/', views.CreateVehicleViewSet)
router.register(r'vehicles/', views.ViewVehiclesListViewSet)
router.register(r'vehicles/<str:id>/', views.RetrieveVehicleViewSet)
router.register(r'vehicles/<str:id>/update/', views.UpdateVehicleViewSet)
router.register(r'vehicles/<str:id>/delete/', views.DeleteVehicleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
