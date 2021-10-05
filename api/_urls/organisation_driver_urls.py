import api._views.organisation_driver_views as views
from django.urls import path


urlpatterns = [
    path(r'create/',
         views.CreateOrganisationDriverViewSet.as_view({'post': 'create'})),
    path('<str:organisation_id>/', views.ViewOrganisationDriversListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:organisation_id>/<str:id>/', views.RetrieveOrganisationDriverViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:organisation_id>/<str:id>/update/',
         views.UpdateOrganisationDriverViewSet.as_view({'put': 'update'})),
    path(r'<str:organisation_id>/<str:id>/delete/',
         views.DeleteOrganisationDriverViewSet.as_view({'delete': 'destroy'})),
]
