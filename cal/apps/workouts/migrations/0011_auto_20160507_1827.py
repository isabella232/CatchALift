# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0010_auto_20160507_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(default=b'', blank=True, to='workouts.Workout'),
        ),
    ]
