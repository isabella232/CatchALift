# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0008_auto_20160510_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='coach_user',
            field=models.CharField(default=b'', unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='message',
            name='msg_from',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
