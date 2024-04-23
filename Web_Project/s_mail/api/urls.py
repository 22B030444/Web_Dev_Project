from django.urls import path
from .views import InboxListView, ComposeView, MessageDetailView, MailboxView, folder_list, folder_detail, \
    attachment_list, attachment_detail

urlpatterns = [
    # path('api/auth/login/', LoginView.as_view(), name='login'),
    # path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    path('mailbox/mails/', InboxListView.as_view(), name='inbox-list'),
    path('mailbox/mails/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('mailbox/mails/create/', ComposeView.as_view(), name='compose'),
    path('mailbox/', MailboxView.as_view(), name='mailbox'),
    path('mailbox/folders/', folder_list, name='folder_list_create'),  # Список и создание папок
    path('mailbox/folders/<int:pk>/', folder_detail, name='folder_detail'),  # Детали папки, обновление и удаление
    path('mailbox/attachments/', attachment_list, name='attachment_list_create'),  # Список и создание вложений
    path('mailbox/attachments/<int:pk>/', attachment_detail, name='attachment_detail'),  # Детали вложения, обновление и удаление
    # path('api/users/', UserListView.as_view(), name='user-list'),
    # path('api/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]

