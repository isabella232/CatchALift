from django.conf.urls import url
from .views import workouts, exercises

urlpatterns = [
    url(r'^workouts$', workouts.workouts, name='workouts'),
    url(r'^wcreate$', workouts.create, name='wcreate'),
    url(r'^mw(?P<workout_id>\d+)$', workouts.modify, name='wmodify'),
    url(r'^rw(?P<workout_id>\d+)$', workouts.remove, name='wremove'),
    url(r'^sw(?P<workout_id>\d+)$', workouts.save, name='wsave'),
    url(r'^wsave_new$', workouts.save_new, name='wsave_new'),
    url(r'^exercises$', exercises.exercises, name='exercises'),
    url(r'^ecreate$', exercises.create, name='ecreate'),
    url(r'^me(?P<exercise_id>\d+)$', exercises.modify, name='emodify'),
    url(r'^re(?P<exercise_id>\d+)$', exercises.remove, name='eremove'),
    url(r'^se(?P<exercise_id>\d+)$', exercises.save, name='esave'),
    url(r'^esave_new$', exercises.save_new, name='esave_new'),
]
