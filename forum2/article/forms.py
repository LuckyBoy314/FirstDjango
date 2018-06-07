# -*- coding:utf-8 -*-
# @author: ZHU Feng

from django import forms
from .models import Article

# 方法以：不使用表单API，直接从request.pOST里获取数据，自行处理校验和错误处理
# 方法二：使用通用表单 forms.Form
# class ArticleForm(forms.Form):
#     title = forms.CharField(label='标题', max_length=100)   # 注意是字段来自于forms,而不是django.db.models
#     content = forms.CharField(label='内容', max_length=10000)

# 方法三：使用与数据模型相关的表单 forms.ModelForm
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']