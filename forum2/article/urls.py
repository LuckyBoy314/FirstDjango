from django.conf.urls import url
from .views import article_list, article_detail, create_article, ArticleDetail, CreateArticle
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^list/(?P<block_id>\d+)', article_list, name='article_list'),
    # 基于函数方法的url配置方式
    # url(r'^details/(?P<article_id>\d+)', article_detail, name='article_detail'),
    # 基于详情类方法的url配置方式, 注意as_view后面有括号
    url(r'^details/(?P<pk>\d+)', ArticleDetail.as_view(), name='article_detail'),

    # 基于函数
    # url(r'^create/(?P<block_id>\d+)', create_article, name='create_article'),
    # 基于类，注意as_view后面有括号
    url(r'^create/(?P<block_id>\d+)', login_required(CreateArticle.as_view()), name='create_article')
]
