from django.shortcuts import render
from blocks.models import Block
from articles.models import Article

def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles = Article.objects.filter(block=block, status=0).order_by('-id')

    return render(request, 'article_list.html',{'articles': articles, 'b': block})
