from rest_framework import serializers
from .models import Task,TaskList
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','task_name','taskList')

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields= ('id','task_list_name')

# class UserSerializer(serializers.ModelSerializer):
#     tasklists = serializers.PrimaryKeyRelatedField(many=True, queryset=TaskList.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'tasklists']
        
