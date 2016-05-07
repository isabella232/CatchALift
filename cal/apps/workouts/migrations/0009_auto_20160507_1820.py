# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0008_auto_20160507_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='exercise',
        ),
        migrations.AddField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(default=None, to='workouts.Workout'),
        ),
    ]
