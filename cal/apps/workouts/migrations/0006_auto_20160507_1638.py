# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0005_auto_20160507_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='title',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
