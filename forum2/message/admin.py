from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('owner', 'link', 'create_timestamp', 'last_update_timestamp', 'status')

admin.site.register(Message, MessageAdmin)