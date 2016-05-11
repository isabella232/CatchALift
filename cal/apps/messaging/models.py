from django.db import models
from datetime import datetime

class Conversation(models.Model):
    coach_user = models.CharField(max_length=100, default='', unique=True)
    coach = models.CharField(max_length=100, default='')
    user = models.CharField(max_length=100, default='')
    def __unicode__(self):
        return self.coach_user

    class Meta:
        verbose_name_plural = "Conversations"

class Message(models.Model):
    msg_from = models.CharField(max_length=50, default='')
    content = models.TextField(max_length=500, default='')
    conversation = models.ForeignKey(Conversation, default=1)
    date_time = models.DateTimeField(editable=False, blank=False, default=datetime.now)
    def __unicode__(self):
        return self.msg_from

    class Meta:
        verbose_name_plural = "Messages"
