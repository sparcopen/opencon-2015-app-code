# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0004_auto_20150703_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='step2rating',
            name='ipaddress',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
    ]
