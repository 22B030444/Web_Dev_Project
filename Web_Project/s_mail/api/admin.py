from django.contrib import admin
from .models import Mailbox, Folder, Message, Attachment

@admin.register(Mailbox)
class MailboxAdmin(admin.ModelAdmin):
    list_display = ('user', 'email_address', 'created_at')
    search_fields = ('user__username', 'email_address')
    list_filter = ('created_at',)

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'mailbox', 'user', 'folder_type')
    list_filter = ('folder_type', 'user')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'folder', 'sender', 'recipient', 'sent_at', 'read')
    search_fields = ('subject', 'sender__username', 'recipient__username')
    list_filter = ('sent_at', 'read')

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('filename', 'size', 'message')
    search_fields = ('filename',)
    list_filter = ('message',)
