# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_rating_ipaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='application',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='application',
            name='enabled',
        ),
        migrations.RemoveField(
            model_name='application',
            name='invitation_sent',
        ),
        migrations.RemoveField(
            model_name='application',
            name='organizing_comittee',
        ),
        migrations.RemoveField(
            model_name='application',
            name='terminator',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
