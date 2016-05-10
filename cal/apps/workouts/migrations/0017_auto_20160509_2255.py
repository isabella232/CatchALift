# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0016_auto_20160509_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
