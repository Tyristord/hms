# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0005_auto_20160209_2020'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctor_details',
        ),
    ]
