from django.db import models

# Create your models here.

class TaskList(models.Model):
    tasklist_name = models.CharField(max_length=30) # have to set it to unoque=True later.
    created_at = models.DateTimeField(auto_now_add=True)
    # task_name = models.ForeignKey(Task,on_delete=models.DO_NOTHING,null=True)

    def __str__(self):
        return self.tasklist_name
    
    # @property
    # def tasks(self):
    #     return self.choice_set.all()
class Task(models.Model):
    task_name = models.CharField(max_length=100)
    taskList = models.ForeignKey(TaskList, on_delete=models.CASCADE,null=True)
    # taskList = models.ManyToManyField(TaskList)

    def __str__(self):
        return self.task_name
