from django.db import models
from django.contrib.auth.models import User


class ActivateValidation(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')
    activate_key = models.CharField('激活码', max_length=50)
    #expire_time = models.DateTimeField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.IntegerField('性别', choices=((0,'男'),(-1,'女')), default=0)
    birthday = models.DateTimeField('生日', blank=True, null=True)
    avatar = models.CharField('头像', max_length=300, blank=True)