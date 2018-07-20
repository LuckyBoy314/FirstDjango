from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    owner = models.ForeignKey(User, verbose_name='消息所属人')
    content = models.TextField('消息内容', max_length=100)
    link = models.CharField('跳转链接', max_length=500)
    status = models.IntegerField('消息状态', choices=((0, '未读'), (-1, '已读')), default=0)