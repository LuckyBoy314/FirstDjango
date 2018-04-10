from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/(?P<block_id>\d+)', views.article_list)
]
