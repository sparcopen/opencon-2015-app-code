# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0017_auto_20150705_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='rated2_count',
            field=models.IntegerField(default=0),
        ),
    ]
