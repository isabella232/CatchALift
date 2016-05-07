# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0007_auto_20160507_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='weight',
        ),
        migrations.AlterField(
            model_name='exercise',
            name='notes',
            field=models.TextField(default=b'', max_length=500),
        ),
    ]
