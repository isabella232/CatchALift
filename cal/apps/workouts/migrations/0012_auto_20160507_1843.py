# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0011_auto_20160507_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='workout',
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise',
            field=models.ManyToManyField(to='workouts.Exercise'),
        ),
    ]
