from rest_framework import serializers
from taskAPI_base.models import Task


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'