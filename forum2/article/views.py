from django.shortcuts import render, redirect
from .models import Article
from block.models import Block
from comment.models import Comment
from django.urls import reverse
from .forms import ArticleForm
from django.views.generic import View
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# def article_list(request, block_id):
#     block = Block.objects.get(id=block_id)
#
#     # 两种方法获取articles
#     # 方法一：正常获取
#     articles = Article.objects.filter(block=block, status=0)
#
#     # 方法二：也可以使用反向映射关系获取
#     articles = block.article_set.all().filter(status=0)
#     return render(request, 'article_list.html', {'b': block, 'articles': articles})

# 加入分页功能
# def article_list(request, block_id):
#     block_id = int(block_id)
#     block = Block.objects.get(id=block_id)
#
#     ARTICLE_CNT_1PAGE = 1
#     page_no = int(request.GET.get('page_no', 1))  # 当前页码
#
#     # 手工实现分页
#     # start_index = (page_no-1)*ARTICLE_CNT_1PAGE
#     # end_index = page_no*ARTICLE_CNT_1PAGE
#     # articles = Article.objects.filter(block=block, status=0).order_by('-id')[start_index:end_index]
#
#     # 使用Paginator实现分页
#     all_articles = Article.objects.filter(block=block, status=0).order_by('-id')
#     p = Paginator(all_articles, ARTICLE_CNT_1PAGE)  # 构建分页器,只需要所有对象和每页对象数量两个变量
#     page = p.page(page_no)  # 当前页面
#     articles = page.object_list  # 当前页中的所有对象
#
#     # 分页控件参数
#     pages_cnt = p.num_pages  # 总页数
#     current_no = page_no  # 当前页码
#     page_links = [i for i in range(page_no - 2, page_no + 3) if i > 0 and i <= pages_cnt]
#     previous_link = page_links[0] - 1
#     next_link = page_links[-1] + 1
#     has_previous = previous_link > 0  # True if previous_link > 0 else False
#     has_next = next_link <= pages_cnt  # True if next_link <= pages_cnt else False
#
#     return render(request, 'article_list.html', {'articles': articles, 'b': block,
#                                                  'pages_cnt': pages_cnt, 'current_no': current_no,
#                                                  'page_links': page_links,
#                                                  'previous_link': previous_link, 'next_link': next_link,
#                                                  'has_previous': has_previous, 'has_next': has_next})


# 将分页功能抽象成函数
def paginate_queryset(objs, page_no, cnt_per_page=2, half_show_length=4):
    """
    获取全量数据objs中当前页面page_no中的数据，以及相关的分页信息
    :param objs: 所有对象
    :param page_no: 当前页码
    :param cnt_per_page: 每页显示数据条数
    :param half_show_length: 分页栏显示的一半长度
    :return: 全量数据objs中当前页面page_no中的数据，以及相关的分页信息
    """
    p = Paginator(objs, cnt_per_page)  # 构建分页器,只需要所有对象和每页对象数量两个变量
    pages_cnt = p.num_pages  # 总页数
    if page_no > pages_cnt:
        page_no = pages_cnt
    if page_no <= 0:
        page_no = 1

    page_links = [i for i in range(page_no - half_show_length, page_no + half_show_length + 1) if
                  i > 0 and i <= pages_cnt]

    page = p.page(page_no)  # 当前页面
    previous_link = page_links[0] - 1
    next_link = page_links[-1] + 1
    has_previous = previous_link > 0  # True if previous_link > 0 else False
    has_next = next_link <= pages_cnt
    #分页相关数据
    pagination_data = {'pages_cnt': pages_cnt,
                       'current_no': page_no,
                       'page_links': page_links,
                       'previous_link': previous_link,
                       'next_link': next_link,
                       'has_previous': has_previous,
                       'has_next': has_next
                       }

    return (page.object_list, pagination_data)

# 使用分页抽象函数
def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    all_articles = Article.objects.filter(block=block, status=0).order_by('-id')

    page_no = int(request.GET.get('page_no', 1))  # 当前页码

    articles, pagination_data = paginate_queryset(all_articles, page_no)

    return render(request, 'article_list.html', {'articles': articles, 'b': block, 'pagination_data': pagination_data})

# 基于函数的创建文章方法
@login_required
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
            article.owner = request.user
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
            article.owner = request.user
            article.save()
            # return redirect(reverse('article_list', args=(block_id,)))
            return redirect('article_list', block_id=block_id)
        else:
            return render(request, self.template_name, {'b': self.block, 'form': form})


# 基于函数的显示文章详情的方法
def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)

    page_no = int(request.GET.get('page_no', 1))
    all_comments = Comment.objects.filter(article=article, status=0)
    comments, pagination_data = paginate_queryset(all_comments, page_no)

    return render(request, 'article_detail.html', {'a': article, 'comments': comments,
                                                   'pagination_data': pagination_data})


# 基于类(视图详情）显示文章的方法，视图详情类DetailView用于在一个网页中显示一个数据模型实例的详情，这种通用的方法被抽象成了详情类
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

    # 如果需要向页面传入其他参数，则需要重载get_context_data方法
    # 所有的传递数据都保存在context中
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_no = int(self.request.GET.get('page_no', 1))
        all_comments = Comment.objects.filter(article = context['a'], status=0)
        comments, pagination_data = paginate_queryset(all_comments, page_no)
        context['comments'] = comments
        context['pagination_data'] = pagination_data
        return context
