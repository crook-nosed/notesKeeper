from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer,TaskListSerializer
from .models import Task,TaskList

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'AllTasks':'/tasks/',
        'AllTaskLists':'/task-lists/',
        'specificTask': '/tasks/<str:pk>',
        'specificTaskList':'/task-lists/<str:pk>',
        'taskCreate':'/task-create/',
        'taskListCreate':'/task-list-create/',
        'taskUpdate':'task-update/<str:pk>/',
        'List Update':'/task-list-update/<str:pk>',
        'List Delete':'/task-list-delete/<str:pk>',
        'task Delete':'/task-delete/<str:pk>'
    }
    return Response(api_urls)

@api_view(['GET'])
def TaskListSingle(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TaskListList(request):
    tasks = TaskList.objects.all()
    serializer = TaskListSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TaskDetail(request, pk):
    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def TaskListDetail(request, pk):
    tasks = TaskList.objects.get(id = pk)
    serializer = TaskListSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def TaskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def TaskListCreate(request):
    serializer = TaskListSerializer(data=request.data)

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

@api_view(['POST'])
def TaskListUpdate(request, pk):
    tasks = TaskList.objects.get(id = pk)
    serializer = TaskListSerializer(tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def TaskDelete(request, pk):
    tasks = Task.objects.get(id = pk)
    tasks.delete()
    return Response('Succesfully Deleted!')

@api_view(['DELETE'])
def TaskListDelete(request, pk):
    task = TaskList.objects.get(id = pk)
    task.delete()
    return Response('Succesfully Deleted!')