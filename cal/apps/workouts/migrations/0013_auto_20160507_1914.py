# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0012_auto_20160507_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(default=b'', unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='workout',
            name='title',
            field=models.CharField(default=b'', unique=True, max_length=10),
        ),
    ]
