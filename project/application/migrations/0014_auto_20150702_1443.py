# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_application_approval_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='approval_level',
            field=models.TextField(null=True, blank=True),
        ),
    ]
