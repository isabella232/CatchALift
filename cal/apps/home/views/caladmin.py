from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from ...util import common, admin_required

@login_required
@admin_required
def remove(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('home:manager')

@login_required
@admin_required
def modify(request, user_id):
    user = User.objects.get(id = user_id)
    context = common(request)
    context['modify'] = True
    context['user_group'] = user.groups.all()[0].name
    context['id'] = user_id
    context['username'] = user.username
    context['fname'] = user.first_name
    context['lname'] = user.last_name
    return render(request, 'index.html', context)

@login_required
@admin_required
def save(request, user_id):
    user = User.objects.get(id = user_id)
    user.username = request.POST['username'].lower()
    user.first_name = request.POST['fname']
    user.last_name = request.POST['lname']
    user.groups.clear()
    g = Group.objects.get(name=request.POST['type'])
    g.user_set.add(user)
    if request.POST['password'] != '':
        user.set_password(request.POST['password'])
    user.save()
    return redirect('home:manager')

@login_required
@admin_required
def create(request):
    context = common(request)
    context['create'] = True
    return render(request, 'index.html', context)

@login_required
@admin_required
def save_new(request):
    if len(User.objects.all().filter(username=request.POST['username'])):
        context = common(request)
        context['create'] = True
        context['error'] = 'This account already exists'
        return render(request, 'index.html', context)
    user = User.objects.create(username=request.POST['username'].lower(), first_name=request.POST['fname'], last_name=request.POST['lname'])
    user.set_password(request.POST['password'])
    g = Group.objects.get(name=request.POST['type'])
    g.user_set.add(user)
    user.save()
    return redirect('home:manager')
