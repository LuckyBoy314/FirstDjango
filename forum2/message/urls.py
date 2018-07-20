from django.conf.urls import url
from .views import read_message


urlpatterns = [
    url(r'^read/(?P<msg_id>\d+)', read_message, name='read_message'),
]
