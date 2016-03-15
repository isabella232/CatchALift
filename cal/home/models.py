from django.db import models

# Create your models here.
class Veteran(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	
	
