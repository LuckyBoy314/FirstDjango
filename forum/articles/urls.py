from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/(?P<block_id>\d+)', views.article_list),
    #url(r'^create/(?P<block_id>\d+)', views.create_article), #基于函数的url
    url(r'^create/(?P<block_id>\d+)', views.CreateArticle.as_view()), #基于类的url,继承于普通view
    url(r'^detail/(?P<pk>\d+)', views.ArticleDetail.as_view()),
]
