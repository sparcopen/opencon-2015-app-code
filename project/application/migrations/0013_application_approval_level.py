# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_application_duplicate'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='approval_level',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
