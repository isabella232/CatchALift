# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_auto_20160507_0151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'verbose_name_plural': 'Exercises'},
        ),
        migrations.AlterModelOptions(
            name='workout',
            options={'verbose_name_plural': 'Workouts'},
        ),
    ]
