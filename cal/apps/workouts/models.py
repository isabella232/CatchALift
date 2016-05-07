from django.db import models

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=100, default='')
    weight = models.TextField(max_length=200, default='')
    reps = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    notes = models.TextField(max_length=300, default='')

    def __unicode__(self):
        return self.name

class Workout(models.Model):
    title = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=100, default='')
    exercise = models.ForeignKey(Exercise, default=None)
    notes = models.TextField(max_length=300, default='')

    def __unicode__(self):
        return self.title
