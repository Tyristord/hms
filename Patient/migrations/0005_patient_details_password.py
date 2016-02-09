# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0004_auto_20151222_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_details',
            name='password',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
