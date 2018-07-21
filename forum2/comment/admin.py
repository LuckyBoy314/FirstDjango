from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'article',  'to_comment', 'create_timestamp', 'last_update_timestamp', 'status')

admin.site.register(Comment, CommentAdmin)