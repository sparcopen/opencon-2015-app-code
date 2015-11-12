# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0015_application_final_decision'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='average_rating',
            field=models.TextField(null=True, blank=True),
        ),
    ]
