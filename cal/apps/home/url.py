from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landing, name='index'),
    url(r'^manager$', views.landing, name='manager'),
    url(r'^manager/c$', views.create, name='create'),
    url(r'^manager/r(?P<user_id>\d+)$', views.remove, name='remove'),
    url(r'^manager/m(?P<user_id>\d+)$', views.modify, name='modify'),
    url(r'^manager/s(?P<user_id>\d+)$', views.save, name='save'),
    url(r'^manager/save_new$', views.save_new, name='save_new'),
    url(r'^sign_out$', views.sign_out, name='sign_out'),
]
