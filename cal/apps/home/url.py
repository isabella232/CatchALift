from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landing, name='index'),
    url(r'^manager$', views.landing, name='manager'),
    url(r'^manager/r(?P<user_id>\d+)$', views.remove, name='remove'),
    url(r'^sign_out$', views.sign_out, name='sign_out'),
]
