from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from ..models import Message, Conversation
from ...util import common, user_required

@login_required
@user_required
def msg(request):
    context = common(request)
    context['coaches'] = Group.objects.get(name='Coach').user_set.all()
    return render(request, 'index.html', context)

@login_required
@user_required
def view(request, coach_id):
    context = common(request)
    coach = User.objects.get(id=coach_id)
    user = request.user
    conv = Conversation.objects.filter(coach_user=(coach.username+'_'+user.username))
    context['user'] = request.user.username
    context['coach'] = coach.first_name + ' ' + coach.last_name
    context['coach_id'] = coach.id
    context['messaging'] = True
    context['messages'] = reversed(Message.objects.filter(conversation=conv))
    return render(request, 'index.html', context)

@login_required
@user_required
def send(request, coach_id):
    user = request.user
    coach = User.objects.get(id=coach_id)
    message = request.POST['message']
    if not len(Conversation.objects.filter(coach_user=(coach.username+'_'+user.username))):
        Conversation.objects.create(coach_user=(coach.username+'_'+user.username))
    conv = Conversation.objects.get(coach_user=(coach.username+'_'+user.username))
    Message.objects.create(msg_from=user.username, content=message, conversation=conv)
    return redirect('msg:uview_conv', coach_id=coach_id)
