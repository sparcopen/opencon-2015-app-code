# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20150531_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='ipaddress',
            field=models.IPAddressField(null=True, blank=True),
        ),
    ]
