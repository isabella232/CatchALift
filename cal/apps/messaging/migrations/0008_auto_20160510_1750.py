# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0007_message_msg_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='coach',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='user',
        ),
        migrations.AddField(
            model_name='conversation',
            name='coach_user',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
