# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_auto_20150603_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='teminated_at',
            new_name='terminated_at',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='teminated_ip',
            new_name='terminated_ip',
        ),
    ]
