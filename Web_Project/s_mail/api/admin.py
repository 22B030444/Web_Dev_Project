from django.contrib import admin
from .models import Mailbox, Folder, Message, Attachment


@admin.register(Mailbox)
class MailboxAdmin(admin.ModelAdmin):
    list_display = ['user', 'email_address', 'created_at']
    search_fields = ['user__username', 'email_address']


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['name', 'mailbox', 'folder_type']
    search_fields = ['name', 'mailbox__user__username']
    list_filter = ['folder_type']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'sender', 'recipient', 'sent_at', 'read']
    search_fields = ['subject', 'sender__username', 'recipient__username']
    list_filter = ['sent_at', 'read']
    date_hierarchy = 'sent_at'


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['filename', 'size', 'message']
    search_fields = ['filename', 'message__subject']
