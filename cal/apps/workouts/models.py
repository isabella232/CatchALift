from django.db import models
from django.contrib.auth.models import User

DEFAULT_ID = 1

class Exercise(models.Model):
    name = models.CharField(max_length=100, default='', unique=True) #Name of Exercise
    reps = models.IntegerField(default=0) #0 if this element doesn't apply
    sets = models.IntegerField(default=0) #0 if this element doesn't apply
    notes = models.TextField(max_length=500, default='') #Links, recommendation, gym, etc.
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Exercises"

class Workout(models.Model):
    title = models.CharField(max_length=20, default='', unique=True) #Title of Workout
    description = models.CharField(max_length=100, default='') #General purpose of workout
    notes = models.TextField(max_length=300, default='') #Patterns of exercises, Additional references
    exercise = models.ManyToManyField(Exercise, default=DEFAULT_ID) #Exercise elements that makes this workout
    user = models.ManyToManyField(User, default=DEFAULT_ID) #Users who subscribe to this workout plan
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Workouts"
