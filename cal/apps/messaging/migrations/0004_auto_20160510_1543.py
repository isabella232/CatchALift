# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0003_message_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('msg_to', models.CharField(default=b'', max_length=50)),
                ('msg_from', models.CharField(default=b'', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.RemoveField(
            model_name='message',
            name='msg_from',
        ),
        migrations.RemoveField(
            model_name='message',
            name='msg_to',
        ),
        migrations.RemoveField(
            model_name='message',
            name='title',
        ),
        migrations.AddField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(default=1, to='messaging.Conversation'),
        ),
    ]
