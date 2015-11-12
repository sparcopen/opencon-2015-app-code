# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_auto_20150603_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='duplicate',
            field=models.ForeignKey(blank=True, to='application.Application', null=True),
        ),
    ]
