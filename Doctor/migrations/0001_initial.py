# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('quali', models.CharField(max_length=200, null=True)),
                ('spec', models.CharField(max_length=200, null=True)),
                ('contact_no', models.IntegerField(default=0)),
                ('mail_id', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
