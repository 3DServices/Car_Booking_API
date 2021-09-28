import api._views.organisationpassenger_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/',
         views.CreateOrganisationPassengerViewSet.as_view({'post': 'create'})),
    path('', views.ViewAllOrganisationPassengersListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:organisation_id>/', views.ViewOrganisationPassengersListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:organisation_id>/<str:id>/', views.RetrieveOrganisationPassengerViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:organisation_id>/<str:id>/update/',
         views.UpdateOrganisationPassengerViewSet.as_view({'put': 'update'})),
    path(r'<str:organisation_id>/<str:id>/delete/',
         views.DeleteOrganisationPassengerViewSet.as_view({'delete': 'destroy'})),
]
