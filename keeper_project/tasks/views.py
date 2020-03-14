from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

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
def TaskList(request):
    tasks = Task.objects.all()
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