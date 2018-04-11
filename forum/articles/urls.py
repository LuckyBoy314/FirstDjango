from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/(?P<block_id>\d+)', views.article_list),
    url(r'^create/(?P<block_id>\d+)', views.create_article)
]
