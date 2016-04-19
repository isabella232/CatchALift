from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landing, name='index'),
    url(r'^sign_out$', views.sign_out, name='sign_out'),
]