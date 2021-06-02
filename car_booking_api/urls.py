"""car_booking_api URL Configuration
"""
from django.conf.urls import url,re_path, include
from django.contrib import admin
from rest_framework import routers, permissions
import authentication.urls as auth_urls
import api.urls as api_urls
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from authentication.views import VerifyEmail, UserViewSet, RegisterView

# DRF - YASG
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://3dservices.co.ug/pages.php?page=vehicles",
        contact=openapi.Contact(email="info@3dservices.co.ug"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # Default route
    path('', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),

    # Admin route
    url(r'^admin/', admin.site.urls),

<<<<<<< HEAD
    # auth
    path('registration/', RegisterView().as_view(), name="registration"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
=======
    # Auth routes
    path('login/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),

    # User Routes
>>>>>>> main
    path('drivers/', include(auth_urls.driver_urls)),
    path('passengers/', include(auth_urls.passenger_urls)),
    path('systemadmins/', include(auth_urls.system_admin_urls)),
    path('fleetmanagers/', include(auth_urls.fleet_manager_urls)),
          # TD: to add a route for user

    # api routes
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

    # drf-yasg Routes
    path('docs/swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('docs/redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

    # Reserved routes
          #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
          #path('', include(router.urls)),
          # path('api/', include(api_urls)),
          # path('auth/', include(auth_urls)),
          # path('docs/swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
