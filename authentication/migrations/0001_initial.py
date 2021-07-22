# Generated by Django 3.2.4 on 2021-07-22 12:11

import authentication.models
import datetime
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address')),
                ('is_verified', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Id', models.UUIDField(default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'), primary_key=True, serialize=False)),
                ('is_passenger', models.BooleanField(default=False, verbose_name='user is a passenger')),
                ('is_systemadmin', models.BooleanField(default=False, verbose_name='user is a system admin')),
                ('is_fleetmanager', models.BooleanField(default=False, verbose_name='user is a passenger')),
                ('is_driver', models.BooleanField(default=False, verbose_name='user is a driver')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', authentication.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SystemAdmin',
            fields=[
                ('registered_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastupdated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'), primary_key=True, serialize=False)),
                ('lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authentication_systemadmin_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('registered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authentication_systemadmin_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='SysAdmin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-lastupdated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PasswordResetInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reset_code', models.CharField(default='000000', max_length=6, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('expires_at', models.DateTimeField(default=datetime.datetime(2021, 7, 23, 12, 11, 31, 693916, tzinfo=utc))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Password Reset Info',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('registered_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastupdated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'), primary_key=True, serialize=False)),
                ('lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authentication_passenger_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('registered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authentication_passenger_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Passenger', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-lastupdated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FleetManager',
            fields=[
                ('registered_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastupdated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'), primary_key=True, serialize=False)),
                ('lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authentication_fleetmanager_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('registered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authentication_fleetmanager_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='FleetManager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-lastupdated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('registered_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastupdated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'), primary_key=True, serialize=False)),
                ('permit_number', models.CharField(default='UAX', max_length=50)),
                ('permit_class', models.CharField(default='UAX', max_length=50)),
                ('permit_expiry_date', models.CharField(default='UAX', max_length=50)),
                ('permit_issuance_date', models.CharField(default='UAX', max_length=50)),
                ('lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authentication_driver_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('registered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authentication_driver_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Driver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-lastupdated_at'],
                'abstract': False,
            },
        ),
    ]
