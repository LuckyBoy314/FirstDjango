from django.conf.urls import url
from .views import article_list, article_detail, create_article

urlpatterns = [
    url(r'^list/(?P<block_id>\d+)', article_list, name='article_list'),
    url(r'^details/(?P<article_id>\d+)', article_detail, name='article_detail'),
    url(r'^create/(?P<block_id>\d+)', create_article, name='create_article')
]
