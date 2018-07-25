from django.shortcuts import render
from block.models import Block
from message.models import Message

def index(request):
    # 原始方法，在程序中给出数据，不使用数据模型来操作数据库
    # blocks_info = [{'name': 'Django专区', 'manager': '弯弯', 'desc': 'Django大法好'},
    #                {'name': 'Python专区', 'manager': '小袁', 'desc': '人生苦短，我用python'},
    #                {'name': '运维专区', 'manager': '小朱', 'desc': '运维人员看过来'}]

    # 使用数据模型model，通过数据库查询来获取数据
    # 首先定义数据模型类
    # 然后添加数据
    # 查询获取数据 类名.object.查询函数
    blocks_info = Block.objects.filter(status=0).order_by('id')

    if request.user.is_authenticated():
        msg_cnt = Message.objects.filter(status=0, owner=request.user).count() # 未读信息数目
    else:
        msg_cnt = 0

    return render(request, 'index.html', {'blocks': blocks_info, 'msg_cnt': msg_cnt})
