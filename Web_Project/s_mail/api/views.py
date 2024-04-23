from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import User,Mailbox,Message,Attachment,Folder
from .serializer import MessageSerializer, MailboxSerializer, FolderSerializer, AttachmentSerializer


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

# class LoginView(APIView):
#     def post(self, request):
#
#
# # Implement user authentication logic and return authentication token
#
# class LogoutView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request):
#
#
# # Implement user logout logic and invalidate authentication token
# class UserListView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#
# # Implement logic to retrieve list of users and serialize them
#
# class UserDetailView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request, pk):
#
# # Implement logic to retrieve details of a specific user by ID and serialize it
class InboxListView(APIView):
    def get(self, request):
        messages = Message.objects.filter(recipient=request.user
                                          )
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

        # Retrieve the user's mailbox, handle DoesNotExist exception gracefully
        try:
            mailbox = Mailbox.objects.get(user=user)
        except Mailbox.DoesNotExist:
            raise NotFound("Mailbox does not exist for the current user.")

        # Retrieve all folders associated with the user's mailbox in a single query
        folders = Folder.objects.filter(mailbox=mailbox)
        folder_serializer = FolderSerializer(folders, many=True)

        # Retrieve all messages associated with the user's mailbox in a single query
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
