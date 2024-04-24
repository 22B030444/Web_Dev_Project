from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, Mailbox, Message, Attachment, Folder
from .serializer import MessageSerializer, MailboxSerializer, FolderSerializer, AttachmentSerializer, UserSerializer


class InboxListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        messages = Message.objects.filter(recipient=request.user)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


class ComposeView(APIView):

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return Response({'Message sent successfully': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Message, pk=pk)

    def get(self, request, pk):
        message = self.get_object(pk)
        serializer = MessageSerializer(message)
        return Response({'message': serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        message = self.get_object(pk)
        message.delete()
        return Response({'message': 'Message successfully deleted'}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        message = self.get_object(pk)
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Message successfully edited'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MailboxView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        try:
            mailbox = Mailbox.objects.get(user=user)
        except Mailbox.DoesNotExist:
            return Response({'error': "Mailbox does not exist for the current user."}, status=status.HTTP_404_NOT_FOUND)

        folders = Folder.objects.filter(mailbox=mailbox)
        folder_serializer = FolderSerializer(folders, many=True)

        messages = Message.objects.filter(folder__in=folders)
        message_serializer = MessageSerializer(messages, many=True)

        attachments = Attachment.objects.filter(message__in=messages)
        attachments_serializer = AttachmentSerializer(attachments, many=True)

        return Response({
            'mailbox': MailboxSerializer(mailbox).data,
            'folders': folder_serializer.data,
            'messages': message_serializer.data,
            'attachments': attachments_serializer.data
        })


@api_view(['GET', 'POST'])
def folder_list(request):
    if request.method == 'GET':
        folders = Folder.objects.all()
        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def folder_detail(request, pk):
    folder = get_object_or_404(Folder, pk=pk)

    if request.method == 'GET':
        serializer = FolderSerializer(folder)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FolderSerializer(folder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def attachment_list(request):
    if request.method == 'GET':
        attachments = Attachment.objects.all()
        serializer = AttachmentSerializer(attachments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def attachment_detail(request, pk):
    attachment = get_object_or_404(Attachment, pk=pk)

    if request.method == 'GET':
        serializer = AttachmentSerializer(attachment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AttachmentSerializer(attachment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        attachment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if 'access' in response.data:
            # Retrieve username from request data
            username = request.data.get('username')
            if not username:
                return Response({'error': 'Username not provided'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
            refresh = RefreshToken.for_user(user)
            response.data['refresh'] = str(refresh)
        return response


class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserListView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetailView(APIView):

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)
