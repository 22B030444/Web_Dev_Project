from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView

from .views import InboxListView, ComposeView, MessageDetailView, MailboxView, folder_list, folder_detail, \
    attachment_list, attachment_detail, UserLoginView, UserLogoutView, UserListView, UserDetailView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('auth/login/', obtain_jwt_token, name='user_login'),
    path('auth/logout/', UserLogoutView.as_view(), name='user_logout'),
    path('mailbox/mails/', InboxListView.as_view(), name='inbox-list'),
    path('mailbox/mails/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('mailbox/mails/create/', ComposeView.as_view(), name='compose'),
    path('mailbox/', MailboxView.as_view(), name='mailbox'),
    path('mailbox/folders/', folder_list, name='folder_list_create'),
    path('mailbox/folders/<int:pk>/', folder_detail, name='folder_detail'),
    path('mailbox/mails/attachments/', attachment_list, name='attachment_list_create'),
    path('mailbox/mails/attachments/<int:pk>/', attachment_detail, name='attachment_detail'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]

