from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import User,Mailbox,Message,Attachment,Folder
from .serializer import MessageSerializer, MailboxSerializer, FolderSerializer


# class MessageView(APIView):
#     def get(self, request):
#         messages = Message.objects.all()
#         serializer = MessageSerializer(messages, many=True)
#         return Response({'messages': serializer.data}, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = MessageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Message successfully sent '})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class MessageDetailView(APIView):
#     def get_object(self, pk=None):
#         message = get_object_or_404(Message, pk=pk)
#     def get(self, request, pk):
#         message = self.get_object(pk)
#         serializer = MessageSerializer(message)
#         return Response({'message': serializer.data}, status=status.HTTP_200_OK)
#
#     def delete(self, request, id):
#         message = get_object_or_404(Message, pk=id)
#         message.delete()
#         return Response({'message': 'Message successfully deleted'}, status=status.HTTP_200_OK)
#
#     def put(self, request, id):
#         message = get_object_or_404(Message, pk=id)
#         serializer = MessageSerializer(message, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Message successfully edited'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class InboxListView(APIView):
    def get(self, request):
        messages = Message.objects.filter(recipient=request.user, folder_type='INBOX')
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
    def get_object(self, pk=None):
        message = get_object_or_404(Message, pk=pk)
    def get(self, request, pk):
        message = self.get_object(pk)
        serializer = MessageSerializer(message)
        return Response({'message': serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id):
        message = get_object_or_404(Message, pk=id)
        message.delete()
        return Response({'message': 'Message successfully deleted'}, status=status.HTTP_200_OK)

    def put(self, request, id):
        message = get_object_or_404(Message, pk=id)
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Message successfully edited'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MailboxView(APIView):
    def get(self, request):
        user = request.user
        mailbox = Mailbox.objects.get(user=user)

        # Retrieve all folders associated with the user's mailbox
        folders = Folder.objects.filter(mailbox=mailbox)
        folder_serializer = FolderSerializer(folders, many=True)

        # Retrieve all messages associated with the user's mailbox
        messages = Message.objects.filter(folder__in=folders)
        message_serializer = MessageSerializer(messages, many=True)

        return Response({
            'mailbox': MailboxSerializer(mailbox).data,
            'folders': folder_serializer.data,
            'messages': message_serializer.data
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