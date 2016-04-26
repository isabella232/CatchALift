from django.shortcuts import render, redirect
from django.contrib.auth import logout

def landing(request):
    if request.user.is_authenticated():
        return render(request, 'home/index.html', {'group': str(request.user.groups.all()[0].name)})
    return redirect('login:login')

def sign_out(request):
    logout(request)
    return redirect('login:login')
