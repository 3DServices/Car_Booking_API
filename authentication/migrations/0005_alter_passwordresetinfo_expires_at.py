# Generated by Django 3.2.4 on 2021-07-26 09:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_passwordresetinfo_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetinfo',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 27, 9, 11, 26, 430424, tzinfo=utc)),
        ),
    ]
