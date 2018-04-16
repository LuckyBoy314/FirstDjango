from django import forms
from articles.models import Article
# 老方法
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=100, label='标题')
#     content = forms.CharField(max_length=10000, label='内容')

#使用与数据模型相关的表单
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
