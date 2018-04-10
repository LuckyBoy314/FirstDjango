from django.shortcuts import render
from .models import Block


def index(request):
    blocks_info = Block.objects.filter(status=0).order_by('-id')
    return render(request, 'index.html',{'blocks':blocks_info})
