from django.urls import path
from .views import folder_list_create, folder_detail  # Импорт представлений

urlpatterns = [
    path('folders/', folder_list_create, name='folder_list_create'),  # Список и создание папок
    path('folders/<int:pk>/', folder_detail, name='folder_detail'),  # Детали папки, обновление и удаление
]
