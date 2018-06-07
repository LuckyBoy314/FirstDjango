from django.shortcuts import render, redirect
from .models import Article
from block.models import Block
from django.urls import reverse
from .forms import ArticleForm


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

    block = Block.objects.get(id=block_id)



    if request.method == 'GET':
        return render(request, 'create_article.html', {'b': block})
    else:
    # 方法1：不使用Django FormA PI，自己实现
    # 直接使用表单Form的POST操作，会有许多问题，第一个问题就是要自己去实现参数校验、错误处理，参数校验、错误处理的代码甚至超过主要业务逻辑代码
    # 另一个问题就是无法通过用户校验，下面的代码是主要逻辑代码，未包含错误处理部分
    #     title = request.POST['title']
    #     content = request.POST['content']
    #     # 参数校验、错误处理部分
    #     # …… #
    #     article = Article(block=block, title=title, content=content, status=0)
    #     article.save()
    #     return redirect(reverse('article_list', args=(block_id)))

    # 方法2：使用通用表单API django.forms.Form
    #     form = ArticleForm(request.POST)
    #     if form.is_valid():
    #         article = Article(block=block, title=form.cleaned_data['title'],
    #                           content=form.cleaned_data['content'], status=0)
    #         article.save()
    #         return redirect(reverse('article_list', args=(block_id)))
    #     else:
    #         return render(request, 'create_article.html', {'b':block, 'form': form})

    # 方法三：使用与数据模型相关的表单API django.forms.ModelForm
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)  # form表单是与Article数据模型直接关联的，所有可直接利用form实例进行创建数据
            article.block = block
            article.status = 0
            article.save()
            return redirect(reverse('article_list', args=(block_id)))
        else:
            return render(request, 'create_article.html', {'b':block, 'form': form})
