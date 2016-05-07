from django.shortcuts import render
from .models import Workout
from ..util import common

# Create your views here.
def workouts(request):
    context = common(request)
    context['workouts'] = Workout.objects.all()
    return render(request,'index.html', context)

def wcreate(request):
    context = common(request)
    pass

def wmodify(request, workout_id):
    context = common(request)
    workout = Workout.objects.get(id=workout_id)
    context['title'] = workout.title
    context['description'] = workout.description
    context['exercises'] = workout.exercise.all()
    context['notes'] = workout.notes
    context['wmodify'] = True
    return render(request, 'index.html', context)

def wremove(request, workout_id):
    pass

def wsave(request):
    pass
