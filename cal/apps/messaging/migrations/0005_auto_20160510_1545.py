# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0004_auto_20160510_1543'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={'verbose_name_plural': 'Conversations'},
        ),
    ]
