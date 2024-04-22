from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import User,Mailbox,Message,Attachment,Folder
from .serializer import MessageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Folder
from .serializer import FolderSerializer


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


@api_view(['GET', 'POST'])
def folder_list_create(request):
    if request.method == 'GET':
        folders = Folder.objects.all()  # Получение всех папок
        serializer = FolderSerializer(folders, many=True)  # Сериализация списка
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FolderSerializer(data=request.data)  # Десериализация данных
        if serializer.is_valid():
            serializer.save()  # Создание новой папки
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def folder_detail(request, pk):
    try:
        folder = Folder.objects.get(pk=pk)  # Получение папки по идентификатору
    except Folder.DoesNotExist:
        return Response({'error': 'Folder not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FolderSerializer(folder)  # Сериализация папки
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FolderSerializer(folder, data=request.data)  # Обновление папки
        if serializer.is_valid():
            serializer.save()  # Сохранение изменений
            return Response(serializer.data)
        return Response(serializer.errors, статус=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        folder.delete()  # Удаление папки
        return Response(status=status.HTTP_204_NO_CONTENT)
