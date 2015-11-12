# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20150531_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step1Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField()),
                ('created', models.DateTimeField(editable=False)),
                ('application_incomplete', models.BooleanField(default=False)),
                ('application_unreadable', models.BooleanField(default=False)),
                ('needs_review', models.BooleanField(default=False)),
                ('person_engaged', models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
                ('why_engaged', models.TextField()),
                ('comments', models.TextField()),
                ('conflict', models.BooleanField(default=False)),
                ('ipaddress', models.GenericIPAddressField(null=True, blank=True)),
                ('application', models.ForeignKey(related_name='ratings', to='application.Application')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('timestamp', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('data', models.TextField()),
                ('enabled', models.BooleanField(default=False)),
                ('organizer', models.BooleanField(default=False)),
                ('terminator', models.BooleanField(default=False)),
                ('invitation_sent', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='step1rating',
            name='created_by',
            field=models.ForeignKey(related_name='rated', to='rating.User'),
        ),
    ]
