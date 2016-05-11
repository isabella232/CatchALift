# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_auto_20160510_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
