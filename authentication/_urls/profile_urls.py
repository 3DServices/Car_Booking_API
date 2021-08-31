import authentication._views.profile_views as views
from django.urls import path


urlpatterns = [
    path(r'create/',
         views.CreateProfileViewSet.as_view({'post': 'create'})),

    path(r'', views.ViewAllProfilesListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),

    path(r'<str:user_id>/', views.ViewProfilesListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),

    path(r'<str:user_id>/<str:id>/', views.RetrieveProfileViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),

    path(r'<str:user_id>/<str:id>/update/',
         views.UpdateProfileViewSet.as_view({'put': 'update'})),

    path(r'<str:user_id>/<str:id>/delete/',
         views.DeleteProfileViewSet.as_view({'delete': 'destroy'})),
]
