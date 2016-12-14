from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from taskAPI_base.models import Task, Category, SubCategory
from taskAPI_base.serializers import TaskSerializer


class Task_List_Create(ListCreateAPIView):
    """
    GET: Retorna todas as tarefas existentes.
    POST: Cria uma nova tarefa.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    
class Task_Detail(RetrieveUpdateDestroyAPIView):
    """
    GET: Retorna uma nova tarefa passando o id.
    POST: Edita uma tarefa passando o id (na URL).
    DELETE: Exclui uma tarefa passando o id.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
