# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0006_auto_20160510_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='msg_from',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
