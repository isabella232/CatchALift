from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Exercise
from ...util import common, coach_required

#Exercises
@login_required
@coach_required
def exercises(request):
    context = common(request)
    context['exercises'] = Exercise.objects.all()
    return render(request,'index.html', context)

@login_required
@coach_required
def create(request):
    context = common(request)
    context['ecreate'] = True
    return render(request, 'index.html', context)

@login_required
@coach_required
def modify(request, exercise_id):
    context = common(request)
    exercise = Exercise.objects.get(id=exercise_id)
    context['id'] = exercise.id
    context['name'] = exercise.name
    context['sets'] = exercise.sets
    context['reps'] = exercise.reps
    context['notes'] = exercise.notes
    context['emodify'] = True
    return render(request, 'index.html', context)

@login_required
@coach_required
def remove(request, exercise_id):
    Exercise.objects.get(id=exercise_id).delete()
    return redirect('plans:exercises')

@login_required
@coach_required
def save(request, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    exercise.name = request.POST['name']
    exercise.reps = request.POST['reps']
    exercise.sets = request.POST['sets']
    exercise.notes = request.POST['notes']
    exercise.save()
    return redirect('plans:exercises')

@login_required
@coach_required
def save_new(request):
    if len(Exercise.objects.all().filter(name=request.POST['name'])):
        context = common(request)
        context['ecreate'] = True
        context['error'] = 'This exercise already exists'
        return render(request, 'index.html', context)
    Exercise.objects.create(name=request.POST['name'], reps=request.POST['reps'], sets=request.POST['sets'], notes=request.POST['notes'])
    return redirect('plans:exercises')
