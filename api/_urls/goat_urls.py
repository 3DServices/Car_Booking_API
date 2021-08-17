import api._views.goat_views as views
from django.urls import path


urlpatterns = [
    path(r'create/',
         views.CreateGoatViewSet.as_view({'post': 'create'})),

    path(r'', views.ViewAllGoatsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:user_id>/', views.ViewGoatsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),

    path(r'<str:user_id>/<str:id>/', views.RetrieveGoatViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),

    path(r'<str:user_id>/<str:id>/update/',
         views.UpdateGoatViewSet.as_view({'put': 'update'})),

    path(r'<str:user_id>/<str:id>/delete/',
         views.DeleteGoatViewSet.as_view({'delete': 'destroy'})),
]
