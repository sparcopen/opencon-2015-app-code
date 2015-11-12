# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20150530_0626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='confilct',
            new_name='conflict',
        ),
        migrations.AlterField(
            model_name='rating',
            name='person_engaged',
            field=models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]
