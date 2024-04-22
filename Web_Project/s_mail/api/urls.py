from django.urls import path
from .views import InboxListView, ComposeView, MessageDetailView, MailboxView, folder_list_create, folder_detail

urlpatterns = [
    # path('api/auth/login/', LoginView.as_view(), name='login'),
    # path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    path('api/mails/', InboxListView.as_view(), name='inbox-list'),
    path('api/mails/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('api/mails/create/', ComposeView.as_view(), name='compose'),
    path('api/mailbox/', MailboxView.as_view(), name='mailbox'),
    path('api/mailbox/folders/', folder_list_create, name='folder_list_create'),  # Список и создание папок
    path('api/mailbox/folders/<int:pk>/', folder_detail, name='folder_detail'),  # Детали папки, обновление и удаление
]

