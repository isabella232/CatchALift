from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from ..models import Message, Conversation
from ...util import common, coach_required

@login_required
@coach_required
def msg(request):
    context = common(request)
    context['users'] = Group.objects.get(name='User').user_set.all()
    return render(request, 'index.html', context)

@login_required
@coach_required
def view(request, user_id):
    context = common(request)
    user = User.objects.get(id=user_id)
    coach = request.user
    conv = Conversation.objects.filter(coach_user=(coach.username+'_'+user.username))
    context['coach'] = request.user.username
    context['user'] = user.first_name + ' ' + user.last_name
    context['user_id'] = user.id
    context['messaging'] = True
    context['messages'] = reversed(Message.objects.filter(conversation=conv))
    return render(request, 'index.html', context)

@login_required
@coach_required
def send(request, user_id):
    coach = request.user
    user = User.objects.get(id=user_id)
    message = request.POST['message']
    if not len(Conversation.objects.filter(coach_user=(coach.username+'_'+user.username))):
        Conversation.objects.create(coach_user=(coach.username+'_'+user.username))
    conv = Conversation.objects.get(coach_user=(coach.username+'_'+user.username))
    Message.objects.create(msg_from=coach.username, content=message, conversation=conv)
    return redirect('msg:cview_conv', user_id=user_id)
