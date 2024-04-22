from django.db import models
from django.contrib.auth.models import User

class Mailbox(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_address = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # Дополнительные поля и методы

class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    # Дополнительные поля и методы

class Folder(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    folder_type_choices = [
        ('INBOX', 'Inbox'),
        ('SENT', 'Sent'),
        ('DRAFTS', 'Drafts'),
        # Другие типы папок
    ]
    folder_type = models.CharField(max_length=10, choices=folder_type_choices)

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    filename = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='attachments')
    # Дополнительные поля и методы


# Create your models here.
