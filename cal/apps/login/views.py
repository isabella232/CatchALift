from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def landing(request):
    if request.method == 'POST':
        name = request.POST['username'].lower()
        user = authenticate(username=name, password=request.POST['password'])
        if user is not None:
            login(request, user)
        else:
            return render(request, 'login/index.html', {'invalid': 'Invalid username or password.'})

    if request.user.is_authenticated():
        return redirect('home:index')
    return render(request, 'login/index.html')
