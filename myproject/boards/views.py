from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.models import User
from .models import Board, Topic, Post
from .forms import NewTopicForm


# 目前view的主要作用是从数据库中查询提取数据
# 但如何创建数据库还是个问题
# 创建数据的方法似乎只有手工或者由表单创建两种方式
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    board = get_object_or_404(Board, pk=pk)  # 更简洁的方式
    return render(request, 'topics.html', {'board': board})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    # 方法1：不使用Django FormA PI，自己实现
    # if request.method == 'POST':
    #     subject = request.POST['subject']
    #     message = request.POST['message']
    #     user = User.objects.first()

    #     # 将表单内容写入到数据库
    #     topic = Topic.objects.create(
    #         subject=subject,
    #         board=board,
    #         starter=user
    #     )
    #     post = Post.objects.create(
    #         message=message,
    #         topic=topic,
    #         created_by=user
    #     )
    #     #  添加主题后，返回到展现主题列表的页面
    #     return redirect('board_topics', pk=board.pk)

    # 非post，则返回创建主题的表单
    # return render(request, 'new_topic.html', {'board': board})

    # 方法2： 使用Django的Form API
    user = User.objects.first()
    if request.method == 'POST':
        # 直接利用请求POST属性创建表单，因为form已经与Topic相关联，不需要逐个字段进行赋值
        form = NewTopicForm(request.POST)
        # 利用Topic设计时的字段要求自动判断用户输入是否合法，不像方法1需要手动判断
        if form.is_valid():
            # 表单form与Topic相关联，它的save方法直接创建Topic的实例
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()

            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)

        # 如果验证失败，需要输入错误提示，并把用户既有输入回填到表单

    else:  # GET请求，form为空
        form = NewTopicForm()
    # 最终form有两种情形，一是GET请求的空表单，二是POST请求表单验证失败需要回填的表单
    return render(request, 'new_topic.html', {'board': board, 'form': form})
