# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20150531_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='terminated_by',
            field=models.ForeignKey(to='rating.User', null=True),
        ),
    ]
