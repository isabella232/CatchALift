from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..models import Workout
from ...util import common, user_required

@login_required
@user_required
def search(request):
    context = common(request)
    context['workouts'] = Workout.objects.all()
    if request.method == 'POST':
        query = request.POST['search']
        context['workouts'] = Workout.objects.filter(title=query)
    return render(request, 'index.html', context)

@login_required
@user_required
def results(request, workout_id):
    context = common(request)
    context['view_workout'] = True
    context['workout'] = Workout.objects.get(id=workout_id)
    context['exercises'] = context['workout'].exercise.all()
    context['subscribed'] = request.user in context['workout'].user.all()
    return render(request, 'index.html', context)

def subscribe(request, workout_id):
    Workout.objects.get(id=workout_id).user.add(request.user)
    return redirect('plans:search')

def unsubscribe(request, workout_id):
    Workout.objects.get(id=workout_id).user.remove(request.user)
    return redirect('plans:search')

def myplans(request):
    context = common(request)
    context['my_workouts'] = []
    workouts = Workout.objects.all()
    for workout in workouts:
        if request.user in workout.user.all():
            context['my_workouts'].append(workout)
    return render(request, 'index.html', context)
