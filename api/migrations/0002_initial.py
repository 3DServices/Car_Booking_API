# Generated by Django 3.2.4 on 2021-06-28 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleblacklist',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_vehicleblacklist_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='vehicleblacklist',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_vehicleblacklist_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='vehicleblacklist',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicle'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_vehicle_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_vehicle_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='trip',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_trip_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='trip',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.driver'),
        ),
        migrations.AddField(
            model_name='trip',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_trip_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='trip',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicle'),
        ),
        migrations.AddField(
            model_name='stationvehicledeploy',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_stationvehicledeploy_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='stationvehicledeploy',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_stationvehicledeploy_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='stationvehicledeploy',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.station'),
        ),
        migrations.AddField(
            model_name='stationvehicledeploy',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicle'),
        ),
        migrations.AddField(
            model_name='station',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_station_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='station',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_station_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='station',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisation'),
        ),
        migrations.AddField(
            model_name='region',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_region_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='region',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_region_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='region',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisation'),
        ),
        migrations.AddField(
            model_name='projectvehicledeploy',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_projectvehicledeploy_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='projectvehicledeploy',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_projectvehicledeploy_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='projectvehicledeploy',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project'),
        ),
        migrations.AddField(
            model_name='projectvehicledeploy',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicle'),
        ),
        migrations.AddField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_project_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='project',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_project_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='project',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisation'),
        ),
        migrations.AddField(
            model_name='passengertrip',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_passengertrip_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='passengertrip',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_passengertrip_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='passengertrip',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.passenger'),
        ),
        migrations.AddField(
            model_name='passengertrip',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.trip'),
        ),
        migrations.AddField(
            model_name='passengerblacklist',
            name='blacklist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.blacklist'),
        ),
        migrations.AddField(
            model_name='passengerblacklist',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_passengerblacklist_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='passengerblacklist',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_passengerblacklist_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='passengerblacklist',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.passenger'),
        ),
        migrations.AddField(
            model_name='organisationvehicle',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_organisationvehicle_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='organisationvehicle',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_organisationvehicle_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='organisationvehicle',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisation'),
        ),
        migrations.AddField(
            model_name='organisationvehicle',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicle'),
        ),
        migrations.AddField(
            model_name='organisationfleetmanager',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_organisationfleetmanager_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='organisationfleetmanager',
            name='fleet_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.fleetmanager'),
        ),
        migrations.AddField(
            model_name='organisationfleetmanager',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_organisationfleetmanager_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='organisationfleetmanager',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisation'),
        ),
        migrations.AddField(
            model_name='organisationdriver',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_organisationdriver_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='organisationdriver',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.driver'),
        ),
        migrations.AddField(
            model_name='organisationdriver',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_organisationdriver_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='organisationdriver',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisation'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_organisation_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_organisation_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='fleetmanagertrip',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_fleetmanagertrip_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='fleetmanagertrip',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.driver'),
        ),
        migrations.AddField(
            model_name='fleetmanagertrip',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_fleetmanagertrip_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='fleetmanagertrip',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.passenger'),
        ),
        migrations.AddField(
            model_name='fleetmanagertrip',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicle'),
        ),
        migrations.AddField(
            model_name='drivertrip',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_drivertrip_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='drivertrip',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.driver'),
        ),
        migrations.AddField(
            model_name='drivertrip',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_drivertrip_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='drivertrip',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.trip'),
        ),
        migrations.AddField(
            model_name='driverblacklist',
            name='blacklist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.blacklist'),
        ),
        migrations.AddField(
            model_name='driverblacklist',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_driverblacklist_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='driverblacklist',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.driver'),
        ),
        migrations.AddField(
            model_name='driverblacklist',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_driverblacklist_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='directoratedepartment',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_directoratedepartment_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='directoratedepartment',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.department'),
        ),
        migrations.AddField(
            model_name='directoratedepartment',
            name='directorate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.directorate'),
        ),
        migrations.AddField(
            model_name='directoratedepartment',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_directoratedepartment_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='directoratedepartment',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisation'),
        ),
        migrations.AddField(
            model_name='directorate',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_directorate_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='directorate',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_directorate_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='directorate',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisation'),
        ),
        migrations.AddField(
            model_name='department',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_department_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='department',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_department_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='department',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisation'),
        ),
        migrations.AddField(
            model_name='branch',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_branch_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='branch',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_branch_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='branch',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisation'),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_blacklist_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='lastupdated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_blacklist_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisation'),
        ),
    ]
