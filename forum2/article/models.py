from django.db import models
from block.models import Block
from django.contrib.auth.models import User

class Article(models.Model):
    owner = models.ForeignKey(User, verbose_name='作者')
    block = models.ForeignKey(Block, verbose_name='板块ID')
    title = models.CharField('文章标题', max_length=100)
    content = models.TextField('文章内容', max_length=10000)
    status = models.IntegerField('状态', choices=((0, '正常'), (-1, '删除')), default=0)
    create_timestamp = models.DateTimeField('创建时间', auto_now_add=True)   # 只在创建时记录一次时间
    last_update_timestamp = models.DateTimeField('最后更新时间', auto_now=True)  # 每次更新都记录时间

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

