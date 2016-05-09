from django.conf.urls import url
from .views import index, caladmin

urlpatterns = [
    url(r'^$', index.landing, name='index'),
    url(r'^manager$', index.landing, name='manager'),
    url(r'^sign_out$', index.sign_out, name='sign_out'),
    url(r'^manager/c$', caladmin.create, name='create'),
    url(r'^manager/r(?P<user_id>\d+)$', caladmin.remove, name='remove'),
    url(r'^manager/m(?P<user_id>\d+)$', caladmin.modify, name='modify'),
    url(r'^manager/s(?P<user_id>\d+)$', caladmin.save, name='save'),
    url(r'^manager/save_new$', caladmin.save_new, name='save_new'),
]
