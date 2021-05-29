import api._views.branch as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/', views.CreateBranchViewSet.as_view({'post': 'create'})),
    path('', views.ViewBranchsListViewSet.as_view(
        {'get': 'list'}), name="view_branches"),
    path(r'<str:id>/', views.RetrieveBranchViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_branches"),
    path(r'<str:id>/update/',
         views.UpdateBranchViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteBranchViewSet.as_view({'delete': 'destroy'})),
]
