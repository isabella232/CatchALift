from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
def landing(request):
    if request.user.is_authenticated():
        return render(request, 'home/index.html')
    return redirect('login:login')

def sign_out(request):
    logout(request)
    return redirect('login:login')
