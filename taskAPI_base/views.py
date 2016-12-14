from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from taskAPI_base.models import Task
from taskAPI_base.serializers import TaskSerializer


class Task_List_Create(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    
class Task_Detail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer