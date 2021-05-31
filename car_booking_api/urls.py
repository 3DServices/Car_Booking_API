"""car_booking_api URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, permissions
import authentication.urls as auth_urls
import api.urls as api_urls
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

# DRF - YASG
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="senjackglobal@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),

    # auth
    path('drivers/', include(auth_urls.driver_urls)),
    path('passengers/', include(auth_urls.passenger_urls)),
    path('systemadmins/', include(auth_urls.system_admin_urls)),
    path('fleetmanagers/', include(auth_urls.fleet_manager_urls)),

    # api
    path('vehicles/', include(api_urls.vehicle_urls)),
    path('blacklists/', include(api_urls.blacklist_urls)),
    path('branches/', include(api_urls.branch_urls)),
    path('departments/', include(api_urls.department_urls)),
    path('directorates/', include(api_urls.directorate_urls)),
    path('driverblacklists/', include(api_urls.driver_blacklist_urls)),
    path('organisationdrivers/', include(api_urls.organisation_driver_urls)),
    path('organisationfleetmanagers/',
         include(api_urls.organisation_fleet_manager_urls)),
    path('organisationvehicles/', include(api_urls.organisation_vehicle_urls)),
    path('organisations/', include(api_urls.organisation_urls)),
    path('passengerblacklists/', include(api_urls.passenger_blacklist_urls)),
    path('projects/', include(api_urls.project_urls)),
    path('stations/', include(api_urls.station_urls)),
    path('vehicleblacklists/', include(api_urls.vehicle_blacklist_urls)),

    path('login/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),

    # drf-yasg
    # path('docs/swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('docs/redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

    # Reserve
    # path('api/', include(api_urls)),
    # path('auth/', include(auth_urls)),
]
