# Generated by Django 3.2.4 on 2021-06-21 10:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210621_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blacklist',
            name='id',
            field=models.CharField(default=uuid.UUID('66338c7a-cdd4-4dd4-adb0-4f5421222ac9'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='branch',
            name='id',
            field=models.CharField(default=uuid.UUID('f71358ae-8a80-4d84-bcba-ffd986e7974b'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default=uuid.UUID('2de852be-05a8-4a01-86d0-8fdae160386c'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='directorate',
            name='id',
            field=models.CharField(default=uuid.UUID('6ff18383-c656-488d-9ca1-e2c26d50771e'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='directoratedepartment',
            name='id',
            field=models.CharField(default=uuid.UUID('74c636d3-e6e6-42d4-b701-ef20887b3b65'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='driverblacklist',
            name='id',
            field=models.CharField(default=uuid.UUID('c32951e8-2d8c-48b1-8ddf-7ec8426e1fcb'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='drivertrip',
            name='id',
            field=models.CharField(default=uuid.UUID('be03b77f-5fde-4365-9288-de04fb0b71d9'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fleetmanagertrip',
            name='id',
            field=models.CharField(default=uuid.UUID('b9bc454c-8965-4d95-a581-07e3505ce471'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='id',
            field=models.CharField(default=uuid.UUID('e767cd17-65b5-46be-a961-aaf7a68993dd'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organisationdriver',
            name='id',
            field=models.CharField(default=uuid.UUID('53bdcf2a-e580-440c-8c39-93fdb7cc5d73'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organisationfleetmanager',
            name='id',
            field=models.CharField(default=uuid.UUID('096e3dc4-d9c4-4da7-be87-8299bb88a82f'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organisationvehicle',
            name='id',
            field=models.CharField(default=uuid.UUID('73ae1613-df98-47fb-a63d-cdc271e097a6'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='passengerblacklist',
            name='id',
            field=models.CharField(default=uuid.UUID('0c889b3d-cec6-424a-89bb-7d1ef691a36a'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='passengertrip',
            name='id',
            field=models.CharField(default=uuid.UUID('ba2a87de-485a-4efc-a24e-cecd57678b2d'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(default=uuid.UUID('51cd4230-34e5-4758-b068-4cf3789c1fb8'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projectvehicledeploy',
            name='id',
            field=models.CharField(default=uuid.UUID('04e19cfa-6969-4625-ba52-dee7a52f81c0'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='region',
            name='id',
            field=models.CharField(default=uuid.UUID('dd6d49c4-8ec0-42ee-be43-1de6220bff73'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='station',
            name='id',
            field=models.CharField(default=uuid.UUID('bbef8582-56f0-4eb1-8897-c95ffddf23a6'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stationvehicledeploy',
            name='id',
            field=models.CharField(default=uuid.UUID('159ba62d-9538-48bf-8a83-a1c35757b8ef'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trip',
            name='id',
            field=models.CharField(default=uuid.UUID('cfa1f4b1-85c3-4ff7-832c-897f9575771d'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='id',
            field=models.CharField(default=uuid.UUID('01fe58fb-e79b-4428-80a1-d0aaf6d9932d'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vehicleblacklist',
            name='id',
            field=models.CharField(default=uuid.UUID('4d318578-172e-407a-adf9-50fe10a7367c'), max_length=50, primary_key=True, serialize=False),
        ),
    ]
