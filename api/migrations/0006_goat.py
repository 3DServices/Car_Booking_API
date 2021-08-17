# Generated by Django 3.2.4 on 2021-08-17 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_passwordresetinfo_expires_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20210815_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goat',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastupdated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'), primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_goat_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_goat_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.passenger')),
            ],
            options={
                'ordering': ['-lastupdated_at'],
                'abstract': False,
            },
        ),
    ]
