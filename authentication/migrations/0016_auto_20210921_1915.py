# Generated by Django 3.2.4 on 2021-09-21 19:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_alter_passwordresetinfo_expires_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='passwordresetinfo',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 22, 19, 15, 20, 847260, tzinfo=utc)),
        ),
    ]
