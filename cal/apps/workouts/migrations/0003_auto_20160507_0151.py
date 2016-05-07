# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_auto_20160506_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='notes',
            field=models.TextField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='notes',
            field=models.TextField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='weight',
            field=models.TextField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='workout',
            name='description',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='workout',
            name='title',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
