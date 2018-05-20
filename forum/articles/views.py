from django.shortcuts import render, redirect
from blocks.models import Block
from articles.models import Article
from articles.forms import ArticleForm
from django.views.generic import View, DetailView
from django.core.paginator import Paginator

def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)

    ARTICLE_CNT_1PAGE = 1
    page_no = int(request.GET.get('page_no',1)) # 当前页码

    #手工实现分页
    # start_index = (page_no-1)*ARTICLE_CNT_1PAGE
    # end_index = page_no*ARTICLE_CNT_1PAGE
    # articles = Article.objects.filter(block=block, status=0).order_by('-id')[start_index:end_index]

    #使用Paginator实现分页
    all_articles = Article.objects.filter(block=block, status=0).order_by('-id')
    p = Paginator(all_articles,ARTICLE_CNT_1PAGE) # 构建分页器,只需要所有对象和每页对象数量两个变量
    page = p.page(page_no) # 当前页面
    articles = page.object_list # 当前页中的所有对象

    #分页控件参数
    pages_cnt = p.num_pages # 总页数
    current_no = page_no # 当前页码
    page_links = [i for i in range(page_no-2, page_no+3) if i > 0 and i <= pages_cnt]
    previous_link = page_links[0]-1
    next_link = page_links[-1]+1
    has_previous = previous_link > 0 #  True if previous_link > 0 else False
    has_next = next_link <= pages_cnt # True if next_link <= pages_cnt else False


    return render(request, 'article_list.html',{'articles': articles, 'b': block,
                    'pages_cnt': pages_cnt, 'current_no': current_no, 'page_links':page_links,
                    'previous_link': previous_link, 'next_link': next_link,
                    'has_previous': has_previous, 'has_next': has_next})

#基于函数的处理
def create_article(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)

    if request.method == "GET":
        return render(request, 'create_article.html', {'b': block})
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            # article = Article(block=block, title=form.cleaned_data['title'],
            #                   content=form.cleaned_data['content'],status=0)

            article = form.save(commit=False)
            article.block = block
            article.status = 0
            article.save()
            return redirect('/article/list/%s'%block_id)
        else:
            return render(request, 'create_article.html', {'b': block, 'form': form})

#基于类的处理
class CreateArticle(View):
    template_name = 'create_article.html'

    def init_data(self, block_id):
        self.block_id = int(block_id)
        self.block = Block.objects.get(id=self.block_id)

    def get(self, request, block_id):
        self.init_data(block_id)
        return render(request, self.template_name, {'b': self.block})

    def post(self, request, block_id):
        self.init_data(block_id)
        form = ArticleForm(request.POST)
        if form.is_valid():
            # article = Article(block=block, title=form.cleaned_data['title'],
            #                   content=form.cleaned_data['content'],status=0)

            article = form.save(commit=False)
            article.block = self.block
            article.status = 0
            article.save()
            return redirect('/article/list/%s' % self.block_id)
        else:
            return render(request, self.template_name, {'b': self.block, 'form': form})

class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'a'