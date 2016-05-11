# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('msg_to', models.CharField(default=b'', max_length=50)),
                ('msg_from', models.CharField(default=b'', max_length=50)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('content', models.TextField(default=b'', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Exercises',
            },
        ),
    ]
