# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('reps', models.IntegerField(default=0)),
                ('sets', models.IntegerField(default=0)),
                ('notes', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='workout',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workout',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise',
            field=models.ForeignKey(default=None, to='workouts.Exercise'),
        ),
    ]
