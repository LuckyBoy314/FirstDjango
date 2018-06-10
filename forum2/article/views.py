from django.shortcuts import render, redirect
from .models import Article
from block.models import Block
from django.urls import reverse
from .forms import ArticleForm
from django.views.generic import View
from django.views.generic import DetailView


def article_list(request, block_id):
    block = Block.objects.get(id=block_id)

    # 两种方法获取articles
    # 方法一：正常获取
    articles = Article.objects.filter(block=block, status=0)

    # 方法二：也可以使用反向映射关系获取
    articles = block.article_set.all().filter(status=0)
    return render(request, 'article_list.html', {'b': block, 'articles': articles})


# 基于函数的创建文章方法
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
            # return redirect(reverse('article_list', args=(block_id,))) # redirect可以直接操作url
            return redirect('article_list', block_id=block_id)
        else:
            return render(request, 'create_article.html', {'b': block, 'form': form})


# 基于类（一般类）的创建文章方法
class CreateArticle(View):
    template_name = 'create_article.html'

    def init_data(self, block_id):
        self.block = Block.objects.get(id=int(block_id))

    def get(self, request, block_id):
        self.init_data(block_id)
        return render(request, self.template_name, {'b': self.block})

    def post(self, request, block_id):
        self.init_data(block_id)
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.block = self.block
            article.status = 0
            article.save()
            # return redirect(reverse('article_list', args=(block_id,)))
            return redirect('article_list', block_id=block_id)
        else:
            return render(request, self.template_name, {'b': self.block, 'form': form})


# 基于函数的显示文章详情的方法
def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'article_detail.html', {'a': article})


# 基于类(详情类）显示文章的方法，详情类DetailView用于在一个网页中显示一个数据模型实例的详情，这种通用的方法被抽象成了详情类
# 在展示一个数据对象的通用类方法：五个地方需要注意：
# 1. 类继承于DetailView
# 2. 从url传入数据对象在数据库中的id，基于函数的是(?P<aid>\d+),aid是函数的参数,在基于类的配置中使用(?P<pk>\d+), <pk>表示primarykey，
#    主键的意思，是限定死的，不需要在类中体现
# 3. 在类中直接用model属性指明数据模型是那个类，而不需要像在函数中显式的获得该对象
# 4. 用template_name指明渲染网页的名字
# 5. 用context_object_name指明该数据对象在网页模板中的名字
class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'a'
