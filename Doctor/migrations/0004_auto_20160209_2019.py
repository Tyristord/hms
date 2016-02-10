# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0003_doctor_details_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_details',
            name='available',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='doctor_details',
            name='experience',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='doctor_details',
            name='hospital',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='doctor_details',
            name='online',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='doctor_details',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='doctor_details',
            name='seniority',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='doctor_details',
            name='trusted',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
