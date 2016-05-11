# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0005_auto_20160510_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='msg_from',
            new_name='coach',
        ),
        migrations.RenameField(
            model_name='conversation',
            old_name='msg_to',
            new_name='user',
        ),
    ]
