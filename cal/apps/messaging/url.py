from django.conf.urls import url
from .views import coach, user

urlpatterns = [
    url(r'^c$', coach.msg, name='cconvs'),
    url(r'^c(?P<user_id>\d+)$', coach.view, name='cview_conv'),
    url(r'^csend(?P<user_id>\d+)$', coach.send, name='csend'),
    url(r'^u$', user.msg, name='uconvs'),
    url(r'^u(?P<coach_id>\d+)$', user.view, name='uview_conv'),
    url(r'^usend(?P<coach_id>\d+)$', user.send, name='usend'),
]
