# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0009_auto_20160507_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(default=None, to='workouts.Workout', null=True),
        ),
    ]
