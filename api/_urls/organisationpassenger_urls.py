import api._views.organisationpassenger_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/',
         views.CreateOrganisationPassengerViewSet.as_view({'post': 'create'})),
    path('', views.ViewOrganisationPassengersListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:id>/', views.RetrieveOrganisationPassengerViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateOrganisationPassengerViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteOrganisationPassengerViewSet.as_view({'delete': 'destroy'})),
]
