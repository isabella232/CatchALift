from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^workouts$', views.workouts, name='workouts'),
    url(r'^create$', views.wcreate, name='wcreate'),
    url(r'^m(?P<workout_id>\d+)$', views.wmodify, name='wmodify'),
    url(r'^r(?P<workout_id>\d+)$', views.wremove, name='wremove'),
    url(r'^save$', views.wsave, name='wsave'),
]
