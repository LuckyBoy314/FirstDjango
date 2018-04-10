from django.db import models

class Block(models.Model):
    name = models.CharField('板块名称', max_length=16)
    desc = models.CharField('板块描述', max_length=36)
    manager_name = models.CharField('板块管理员', max_length=12)
    status = models.IntegerField('状态', choices=((0,'正常'),(-1,'不正常')), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '板块'
        verbose_name_plural = '板块'