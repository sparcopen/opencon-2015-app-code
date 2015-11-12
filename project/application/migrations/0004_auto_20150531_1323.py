# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20150530_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='oranizing_committee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='welcome_sent',
            field=models.BooleanField(default=False),
        ),
    ]
