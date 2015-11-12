# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
        ('application', '0008_auto_20150531_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='approved_by',
            field=models.ForeignKey(related_name='approved', to='rating.User', null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='terminated_by',
            field=models.ForeignKey(related_name='terminated', to='rating.User', null=True),
        ),
    ]
