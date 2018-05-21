from django.contrib import admin
from .models import Board, Topic, Post

class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject', 'starter', 'board', 'last_updated')

admin.site.register(Board, BoardAdmin)
admin.site.register(Topic, TopicAdmin)
