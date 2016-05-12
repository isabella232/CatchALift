# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0017_auto_20160509_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='title',
            field=models.CharField(default=b'', unique=True, max_length=20),
        ),
    ]
