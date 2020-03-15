from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer,TaskListSerializer
from .models import Task,TaskList
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list-list/',
        'ListDetails':'/task-list-detail/<str:pk>',
        'Listcreate':'/task-list-create/',
        'Task Create':'/task-create/',
        'List Update':'/task-list-update/<str:pk>',
        'List Delete':'/task-list-delete/<str:pk>',
        'task Update':'/task-update/<str:pk>',
        'task Delete':'/task-delete/<str:pk>'
    }
    return Response(api_urls)

@api_view(['GET'])
def TaskListFunctionView(request):
    taskLists = TaskList.objects.all()
    serializer = TaskListSerializer(taskLists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TaskListList(request):
    tasks = TaskList.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TaskDetail(request, pk):
    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def TaskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def TaskUpdate(request, pk):
    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializer(tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def TaskDelete(request, pk):
    tasks = Task.objects.get(id = pk)
    tasks.delete()
    return Response('Succesfully Deleted!')

# from django.shortcuts import render
# from .models import *
# from .serializers import *
# from rest_framework import generics
# # Create your views here.


class TaskListListView(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListSingleView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskListSerializer
    queryset = TaskList.objects.all()


class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskSingleView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()