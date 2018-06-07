from django.db import models

class Block(models.Model):
    name = models.CharField('板块名称', max_length=16)
    desc = models.CharField('板块描述', max_length=36)
    manager = models.CharField('板块管理员', max_length=12)

    # 在后期再增加一个字段的时候，最好提供默认值，否则在同步数据库的时候不知道在已有记录上添加什么值
    status = models.IntegerField('状态', choices=((0, '正常'), (-1, '不正常')), default=0)

    # 对一个数据对象的字符串表示方法的定义，py2中为__unicode__方法
    def __str__(self):
        return self.name

    # 对数据模型类进行字符串表示方法的定义
    class Meta:
        verbose_name = '板块'
        verbose_name_plural = '板块'