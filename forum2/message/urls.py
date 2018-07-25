from django.conf.urls import url
from .views import message_list, read_message


urlpatterns = [
    url(r'^message_list/$', message_list, name='message_list'),
    url(r'^read/(?P<msg_id>\d+)$', read_message, name='read_message'),
]
