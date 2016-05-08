import os, sys, django
sys.path.append('/home/jackson/Projects/CatchALift/cal')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cal.settings'
django.setup()
from apps.workouts.models import Workout, Exercise
import json

w_json = open('workouts.json', 'r')
w_list = json.load(w_json)
e_json = open('exercises.json', 'r')
e_list = json.load(e_json)

for e in e_list:
    if len(Exercise.objects.filter(name=e['name'])) == 0:
        new_exercse = Exercise.objects.create(name=e['name'], sets=e['sets'], reps=e['reps'], notes=e['notes'])
        print('Added ' + e['name'])

for w in w_list:
    if len(Workout.objects.filter(title=w['title'])) == 0:
        we_list = w['exercises'].split(',')
        new_workout = Workout.objects.create(title=w['title'],description=w['description'],notes=w['notes'])
        for we in we_list:
            new_workout.exercise.add(Exercise.objects.get(name=we))
        print('Added ' + w['title'])
