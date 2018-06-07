from django.contrib import admin
from .models import Article

# 通过继承admin.ModelAdmin对如何在后台展示数据模型的对象进行更加复杂的配置
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'block', 'create_timestamp','last_update_timestamp','status')   # 在后台展示的字段

admin.site.register(Article, ArticleAdmin)