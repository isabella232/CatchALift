import os, sys, django
sys.path.append('/home/jackson/Projects/CatchALift/cal')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cal.settings'
django.setup()
from apps.messaging.models import Conversation, Message
for conversation in Conversation.objects.all():
    print('Deleting conv: ' + conversation.coach_user)
    conversation.delete()
for message in Message.objects.all():
    print('Deleting msg: ' + message.content)
    message.delete()
print('msg reset')
