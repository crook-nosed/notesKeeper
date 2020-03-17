from tasks.models import Task,TaskList
from .serializers import TaskSerializer,TaskListSerializer
from rest_framework import viewsets,permissions

# Task Viewset
class TaskViewSet(viewsets.ModelViewSet):
    # queryset = Task.objects.all()
    permission_classes= [
        permissions.IsAuthenticated
    ]
    serializer_class=TaskSerializer

    def get_queryset(self):
        return self.request.user.tasks.all()
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)
# TaskList ViewSet
class TaskListViewSet(viewsets.ModelViewSet):
    # queryset = TaskList.objects.all()
    permission_classes= [
        permissions.IsAuthenticated
    ]
    serializer_class=TaskListSerializer

    def get_queryset(self):
        return self.request.user.tasklists.all()
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)