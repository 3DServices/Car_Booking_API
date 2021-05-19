
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
import authentication.views as views
from django.urls import path


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
