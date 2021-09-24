# Generated by Django 3.2.4 on 2021-09-24 09:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0019_alter_passwordresetinfo_expires_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='passwordresetinfo',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 25, 9, 33, 52, 591305, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_fleetmanager',
            field=models.BooleanField(default=False, verbose_name='user is a fleet manager'),
        ),
    ]
