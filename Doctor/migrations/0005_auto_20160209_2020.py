# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0004_auto_20160209_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_details',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='doctor_details',
            name='fee',
            field=models.IntegerField(default=0),
        ),
    ]
