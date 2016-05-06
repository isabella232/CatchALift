from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group

def landing(request):
    if not request.user.is_authenticated():
        return redirect('login:login')
    context = dict()
    context['name'] = request.user.get_username()
    context['group'] = request.user.groups.all()[0].name
    context['page'] = request.path

    if request.path == '/manager':
        context['coach_list'] = User.objects.filter(groups__name='Coach')
        context['user_list'] = User.objects.filter(groups__name='User')

    return render(request, 'home/index.html', context)

def sign_out(request):
    logout(request)
    return redirect('login:login')

#CALadmin views(navigating, mod/rem/make users)
def remove(request, user_id):
    if not request.user.is_authenticated():
        return redirect('login:login')
    User.objects.get(id=user_id).delete()
    return redirect('home:manager')

def modify(request, user_id):
    if not request.user.is_authenticated():
        return redirect('login:login')
    user = User.objects.get(id = user_id)
    context = dict()
    context['modify'] = True
    context['group'] = request.user.groups.all()[0].name
    context['user_group'] = user.groups.all()[0].name
    context['page'] = request.path
    context['id'] = user_id
    context['username'] = user.username
    context['fname'] = user.first_name
    context['lname'] = user.last_name
    return render(request, 'home/index.html', context)

def save(request, user_id):
    if not request.user.is_authenticated():
        return redirect('login:login')
    user = User.objects.get(id = user_id)
    user.username = request.POST['username']
    user.first_name = request.POST['fname']
    user.last_name = request.POST['lname']
    user.groups.clear()
    g = Group.objects.get(name=request.POST['type'])
    g.user_set.add(user)
    if request.POST['password'] != '':
        user.set_password(request.POST['password'])
    user.save()
    return redirect('home:manager')

def create(request):
    if not request.user.is_authenticated():
        return redirect('login:login')
    context = dict()
    context['create'] = True
    context['group'] = request.user.groups.all()[0].name
    context['page'] = request.path
    return render(request, 'home/index.html', context)

def save_new(request):
    if not request.user.is_authenticated():
        return redirect('login:login')
    error = len(User.objects.all().filter(username=request.POST['username']))!=0
    if error:
        context = dict()
        context['create'] = True
        context['group'] = request.user.groups.all()[0].name
        context['page'] = request.path
        context['error'] = 'This account already exists'
        return render(request, 'home/index.html', context)
    user = User.objects.create(username=request.POST['username'], first_name=request.POST['fname'], last_name=request.POST['lname'])
    user.set_password(request.POST['password'])
    g = Group.objects.get(name=request.POST['type'])
    g.user_set.add(user)
    user.save()
    return redirect('home:manager')
