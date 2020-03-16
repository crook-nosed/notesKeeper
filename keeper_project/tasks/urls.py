from django.urls import path
from .views import *

urlpatterns = [
    path('',apiOverview,name='apiOverview'),
    path('tasks/',TaskListSingle,name='tasks'),
    path('task-lists/',TaskListList,name='task-lists'),
    path('tasks/<str:pk>',TaskDetail,name='task-detail'),
    path('task-lists/<str:pk>',TaskListDetail,name='task-list-detail'),
    path('task-create/',TaskCreate,name='task-create'),
    path('task-list-create/',TaskListCreate,name='task-list-create'),
    path('task-update/<str:pk>',TaskUpdate,name='task-update'),
    path('task-list-update/<str:pk>',TaskListUpdate,name='task-list-update'),
    path('task-delete/<str:pk>',TaskDelete,name='task-delete'),
    path('task-list-delete/<str:pk>',TaskListDelete,name='task-list-delete'),
    # path('users/', UserList.as_view()),
    # path('users/<int:pk>/', UserDetail.as_view()),
    
]
