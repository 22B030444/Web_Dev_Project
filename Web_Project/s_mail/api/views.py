from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import User,Mailbox,Message,Attachment,Folder
from .serializer import MessageSerializer


class MessageView(APIView):
    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response({'messages': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Message successfully sent '})
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
