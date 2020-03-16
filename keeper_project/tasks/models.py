from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskList(models.Model):
    task_list_name = models.CharField(max_length=30) # have to set it to unoque=True later.
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name="tasklists",on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.tasklist_name

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    taskList = models.ForeignKey(TaskList, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.task_name
