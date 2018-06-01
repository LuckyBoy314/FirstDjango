from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Board


# 目前view的主要作用是从数据库中查询提取数据
# 但如何创建数据库还是个问题
# 创建数据的方法似乎只有手工或者由表单创建两种方式
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html',{'boards': boards})

def board_topics(request, pk):
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    board = get_object_or_404(Board, pk=pk) # 更简洁的方式
    return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)  # 更简洁的方式
    return render(request, 'new_topic.html', {'board': board})
