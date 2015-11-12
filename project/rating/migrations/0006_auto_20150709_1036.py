# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0005_step2rating_ipaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step2rating',
            name='application_problem',
            field=models.TextField(),
        ),
    ]
