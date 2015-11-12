# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0014_auto_20150702_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='final_decision',
            field=models.TextField(null=True, blank=True),
        ),
    ]
