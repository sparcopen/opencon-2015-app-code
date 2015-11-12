# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('timestamp', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('data', models.TextField()),
                ('terminator', models.BooleanField(default=False)),
                ('terminated', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('invitation_sent', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
                ('rated_count', models.IntegerField(default=0)),
                ('created', models.DateTimeField(editable=False)),
                ('terminated_by', models.ForeignKey(to='application.Application', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.TextField()),
                ('created', models.DateTimeField(editable=False)),
                ('application', models.ForeignKey(related_name='ratings', to='application.Application')),
                ('created_by', models.ForeignKey(related_name='rated', to='application.Application')),
            ],
        ),
    ]
