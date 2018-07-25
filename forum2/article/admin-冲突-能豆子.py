from django.contrib import admin
from .models import Article
from comment.models import Comment


# 内联表单设置，
class CommentInline(admin.TabularInline):
    model = Comment
    can_delete = False


# 通过继承admin.ModelAdmin对如何在后台展示数据模型的对象进行更加复杂的配置
class ArticleAdmin(admin.ModelAdmin):
    # 在后台展示的字段
    list_display = ('title', 'block', 'create_timestamp', 'last_update_timestamp', 'status')

    # 内联设置，内联到哪里，被内联数据模型必须以内联目标对象为外键
    inlines = [CommentInline]

    # 自定义动作
    actions = ['make_picked']

    def make_picked(self, request, queryset):
        for a in queryset:
            a.status = 10
            a.save()

    make_picked.short_description = '设置精华'

    # 分组显示字段
    fieldsets = (('基本', {'classes': ('wide',),
                         'fields': ('title', 'content')}),
                 ('高级', {'classes': ('collapse',),
                         'fields': ('owner', 'block', 'status')}),
                 )


# 注册到后台
admin.site.register(Article, ArticleAdmin)
