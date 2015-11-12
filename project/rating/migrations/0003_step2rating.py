# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0015_application_final_decision'),
        ('rating', '0002_user_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step2Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.IntegerField()),
                ('created', models.DateTimeField(editable=False)),
                ('comments', models.TextField(null=True, blank=True)),
                ('engagement', models.TextField(null=True, blank=True)),
                ('interest', models.IntegerField()),
                ('needs_review', models.BooleanField(default=False)),
                ('application_problem', models.BooleanField(default=False)),
                ('application', models.ForeignKey(related_name='ratings2', to='application.Application')),
                ('created_by', models.ForeignKey(related_name='rated2', to='rating.User')),
            ],
        ),
    ]
