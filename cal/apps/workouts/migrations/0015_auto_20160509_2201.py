# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0014_workout_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', unique=True, max_length=30)),
                ('description', models.CharField(default=b'', unique=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise',
            field=models.ManyToManyField(default=1, to='workouts.Exercise'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='user',
            field=models.ManyToManyField(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workout',
            name='category',
            field=models.ForeignKey(default=1, to='workouts.Category'),
        ),
    ]
