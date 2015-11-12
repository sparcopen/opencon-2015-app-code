# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='application_incomplete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rating',
            name='application_unreadable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rating',
            name='comments',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='confilct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rating',
            name='needs_review',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rating',
            name='person_engaged',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rating',
            name='why_engaged',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
