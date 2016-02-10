# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0003_remove_patient_details_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_details',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient_details',
            name='contact_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient_details',
            name='insurance_enquiry',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient_details',
            name='insurance_no',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient_details',
            name='insurance_policy',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient_details',
            name='insurance_provider',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient_details',
            name='mail_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient_details',
            name='patient_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient_details',
            name='patient_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient_details',
            name='patient_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
