from django.conf.urls import url, include
import authentication._views.user_views as views
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
