# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_auto_20150603_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='approved_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='approved_ip',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='teminated_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='teminated_ip',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
    ]
