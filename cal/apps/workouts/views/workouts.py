from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Workout, Exercise
from ...util import common, coach_required

#Workouts
@login_required
@coach_required
def workouts(request):
    context = common(request)
    context['workouts'] = Workout.objects.all()
    return render(request,'index.html', context)

@login_required
@coach_required
def create(request):
    context = common(request)
    context['wcreate'] = True
    context['all_exercises'] = Exercise.objects.all()
    return render(request, 'index.html', context)


@login_required
@coach_required
def modify(request, workout_id):
    context = common(request)
    workout = Workout.objects.get(id=workout_id)
    context['all_exercises'] = Exercise.objects.all()
    context['title'] = workout.title
    context['description'] = workout.description
    context['workout_exercises'] = workout.exercise.all()
    context['notes'] = workout.notes
    context['id'] = workout.id
    context['wmodify'] = True
    return render(request, 'index.html', context)

@login_required
@coach_required
def remove(request, workout_id):
    Workout.objects.get(id=workout_id).delete()
    return redirect('coach:workouts')

@login_required
@coach_required
def save(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    workout.title = request.POST['title']
    workout.description = request.POST['description']
    workout.notes = request.POST['notes']
    workout.exercise.clear()
    for exercise in request.POST.getlist('exercises'):
        workout.exercise.add(Exercise.objects.get(name=exercise))
    workout.save()
    return redirect('coach:workouts')

@login_required
@coach_required
def save_new(request):
    if len(Workout.objects.all().filter(title=request.POST['title'])):
        context = common(request)
        context['wcreate'] = True
        context['error'] = 'This workout plan already exists'
        return render(request, 'index.html', context)
    workout = Workout.objects.create(title=request.POST['title'],description=request.POST['description'],notes=request.POST['notes'])
    for exercise in request.POST.getlist('exercises'):
        workout.exercise.add(Exercise.objects.get(name=exercise))
    return redirect('coach:workouts')
