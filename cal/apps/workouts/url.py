from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^workouts$', views.workouts, name='workouts'),

]
