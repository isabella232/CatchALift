from django.shortcuts import render
from .models import Workout, Exercise
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
    all_exercises = Exercise.objects.all()
    context['title'] = workout.title
    context['description'] = workout.description
    context['exercises'] = workout.exercise.all()
    context['notes'] = workout.notes
    context['wmodify'] = True
    context['exer_inverse'] = [exercise for exercise in all_exercises if exercise not in context['exercises']]
    return render(request, 'index.html', context)

def wremove(request, workout_id):
    pass

def wsave(request):
    pass
