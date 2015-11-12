# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20150531_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='oranizing_committee',
            new_name='organizing_comittee',
        ),
    ]
