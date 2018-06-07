from django.shortcuts import render, redirect
from .models import Article
from block.models import Block
from django.urls import reverse

def article_list(request, block_id):
    block = Block.objects.get(id=block_id)

    # 两种方法获取articles
    # 方法一：正常获取
    articles = Article.objects.filter(block=block, status=0)

    # 方法二：也可以使用反向映射关系获取
    articles = block.article_set.all().filter(status=0)
    return render(request, 'article_list.html', {'b': block, 'articles': articles})


def article_detail(request, article_id):
    article = Article.objects.get(id = article_id)
    return render(request, 'article_detail.html', {'a': article})


def create_article(request, block_id):
    """
    使用表单创建数据
    """
    # 方法1：不使用Django FormA PI，自己实现
    block = Block.objects.get(id=block_id)
    if request.method == 'GET':
        return render(request, 'create_article.html', {'b': block})
    else:
        title = request.POST['title']
        content = request.POST['content']
        article = Article(block=block, title=title, content=content, status=0)
        article.save()
        return redirect(reverse('article_list', args=(block_id)))