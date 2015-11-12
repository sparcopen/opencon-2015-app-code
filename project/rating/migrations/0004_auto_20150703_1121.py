# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0003_step2rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step2rating',
            name='engagement',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
