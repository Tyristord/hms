# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_auto_20151222_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_details',
            name='age',
        ),
    ]
