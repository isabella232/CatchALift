# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0004_auto_20160507_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='title',
            field=models.CharField(default=b'', max_length=10),
        ),
    ]
