from rest_framework import serializers
from .models import Task,TaskList

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','task_name','taskList')

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields= ('id','task_list_name')
        
