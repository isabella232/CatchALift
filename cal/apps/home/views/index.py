from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from ...util import common

@login_required
def landing(request):
    context = common(request)
    context['name'] = request.user.get_username()
    if request.path == '/manager':
        context['coach_list'] = User.objects.filter(groups__name='Coach')
        context['user_list'] = User.objects.filter(groups__name='User')
    return render(request, 'index.html', context)

@login_required
def sign_out(request):
    logout(request)
    return redirect('login:login')

#CALadmin views(navigating, mod/rem/make users)
