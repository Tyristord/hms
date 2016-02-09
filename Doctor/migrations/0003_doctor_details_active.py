# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0002_doctor_details_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_details',
            name='active',
            field=models.IntegerField(default=0),
        ),
    ]
