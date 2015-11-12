# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0016_application_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='average_rating',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
