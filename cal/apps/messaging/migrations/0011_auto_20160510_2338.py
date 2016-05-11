# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0010_auto_20160510_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='coach',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='conversation',
            name='user',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
