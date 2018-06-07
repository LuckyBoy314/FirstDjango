from django.contrib import admin
from .models import Block

# 将数据模型注册到admin的最简单的方法
# admin.site.register(Block)

# 通过继承admin.ModelAdmin对如何在后台展示数据模型的对象进行更加复杂的配置
class BlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'manager')   # 在后台展示的字段

admin.site.register(Block, BlockAdmin)