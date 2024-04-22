from django.urls import path
from .views import InboxListView, ComposeView, MessageDetailView, MailboxView, folder_list, folder_detail

urlpatterns = [
    # path('api/auth/login/', LoginView.as_view(), name='login'),
    # path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    path('mails/', InboxListView.as_view(), name='inbox-list'),
    path('mails/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('mails/create/', ComposeView.as_view(), name='compose'),
    path('mailbox/', MailboxView.as_view(), name='mailbox'),
    path('mailbox/folders/', folder_list, name='folder_list_create'),  # Список и создание папок
    path('mailbox/folders/<int:pk>/', folder_detail, name='folder_detail'),  # Детали папки, обновление и удаление
]

