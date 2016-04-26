from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User

def landing(request):
    if not request.user.is_authenticated():
        return redirect('login:login')
    context = dict()
    context['name'] = str(request.user.get_username())
    context['group'] = str(request.user.groups.all()[0].name)
    context['page'] = str(request.path)

    if request.path == '/manager':
        context['coach_list'] = User.objects.filter(groups__name='Coach')
        context['user_list'] = User.objects.filter(groups__name='User')

    return render(request, 'home/index.html', context)

def sign_out(request):
    logout(request)
    return redirect('login:login')
