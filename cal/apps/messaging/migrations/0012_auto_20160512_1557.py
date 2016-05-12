# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0011_auto_20160510_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='coach_user',
            field=models.CharField(default=b'', unique=True, max_length=200),
        ),
    ]
