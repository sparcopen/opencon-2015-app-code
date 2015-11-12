# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('key', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('access_token', models.TextField()),
                ('refresh_token', models.TextField()),
                ('client_id', models.TextField()),
                ('client_secret', models.TextField()),
                ('scope', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='sheet',
            name='token',
            field=models.ForeignKey(to='spreadsheet.Token'),
        ),
    ]
