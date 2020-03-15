from rest_framework import serializers,fields
from .models import Task,TaskList

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','task_name','taskList')
        # read_only_fields = ('taskList',)


class TaskListSerializer(serializers.ModelSerializer):
    # task = TaskSerializer( many=True, read_only=True)
    class Meta:
        model = TaskList   
        fields = ('id','tasklist_name')   
