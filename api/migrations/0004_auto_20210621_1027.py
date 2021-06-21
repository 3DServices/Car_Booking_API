# Generated by Django 3.2.4 on 2021-06-21 10:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210621_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blacklist',
            name='id',
            field=models.CharField(default=uuid.UUID('f8708aa6-3432-4812-9df7-2b2666742916'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='branch',
            name='id',
            field=models.CharField(default=uuid.UUID('1c2c0f7c-6132-4329-9f97-94dbb671a58e'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default=uuid.UUID('a6224deb-5b89-4a25-b1bd-5aa34f1ca9c9'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='directorate',
            name='id',
            field=models.CharField(default=uuid.UUID('684b2e44-5ede-4d9f-89af-cb2f5adb14a9'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='directoratedepartment',
            name='id',
            field=models.CharField(default=uuid.UUID('e02e381c-4615-48db-be96-59f0ddcafd97'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='driverblacklist',
            name='id',
            field=models.CharField(default=uuid.UUID('1b9d79b0-521a-4f69-b4c5-a862c3f39870'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='drivertrip',
            name='id',
            field=models.CharField(default=uuid.UUID('0b7fad8f-cdd9-4473-917c-fc98f17f9f17'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fleetmanagertrip',
            name='id',
            field=models.CharField(default=uuid.UUID('2b826058-dc71-4588-b417-cab9ae9a1757'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='id',
            field=models.CharField(default=uuid.UUID('4c3e83c1-8a75-49ff-9026-261a674b736c'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organisationdriver',
            name='id',
            field=models.CharField(default=uuid.UUID('7c1722dc-2fd6-40c9-af47-1a2a1fcd96b8'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organisationfleetmanager',
            name='id',
            field=models.CharField(default=uuid.UUID('014c0a45-5ecb-4809-9be5-69c90b66f3ae'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organisationvehicle',
            name='id',
            field=models.CharField(default=uuid.UUID('d27b9e45-3a9a-438b-bc20-9be700adb47d'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='passengerblacklist',
            name='id',
            field=models.CharField(default=uuid.UUID('8f607df1-7d9a-4c3e-a5f2-0fcd63e80215'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='passengertrip',
            name='id',
            field=models.CharField(default=uuid.UUID('4f31b8f6-9fd8-40f7-a3c8-cbc1eaada349'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(default=uuid.UUID('1d9e4e35-3e5c-4b4a-9a43-c32101524405'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projectvehicledeploy',
            name='id',
            field=models.CharField(default=uuid.UUID('27c52fd3-4dc8-4fea-af31-b6ec01624e7f'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='region',
            name='id',
            field=models.CharField(default=uuid.UUID('34bb5288-63fb-4e2c-85e8-f15ebf016711'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='station',
            name='id',
            field=models.CharField(default=uuid.UUID('bc4c4579-3cff-4ee6-a02a-cac9b48ecf5d'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stationvehicledeploy',
            name='id',
            field=models.CharField(default=uuid.UUID('83c483a1-1d14-4c1c-905b-cfddf1bfdb8a'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trip',
            name='id',
            field=models.CharField(default=uuid.UUID('3bfb2626-acf6-4583-85a7-c0d38cb5b12b'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='id',
            field=models.CharField(default=uuid.UUID('3f12abc9-e309-4226-a2f9-b9e6b7fd6652'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vehicleblacklist',
            name='id',
            field=models.CharField(default=uuid.UUID('901a9fbc-4ce3-4a49-baff-35b73e5e92d5'), max_length=50, primary_key=True, serialize=False),
        ),
    ]
