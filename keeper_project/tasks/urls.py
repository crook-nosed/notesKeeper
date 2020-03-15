from django.urls import path
# from .views import apiOverview,TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete
from .views import *

urlpatterns = [
    path('',apiOverview,name='apiOverview'),
    path('task-lists/',TaskListList,name='task-lists'),
    # path('task-lists/',TaskListListView.as_view(),name='task-lists'),
    path('task-lists/<str:pk>',TaskListSingleView.as_view(),name='task-list-single'),
    path('tasks/',TaskListView.as_view(),name='tasks'),
    path('tasks/<str:pk>',TaskSingleView.as_view(),name='task-single'),
    # path('task-create/',TaskCreate,name='task-create'),
    # path('task-update/<str:pk>',TaskUpdate,name='task-update'),
    # path('task-delete/<str:pk>',TaskDelete,name='task-delete'),
    
]

# url(r'^api/musicians/$', MusicianListView.as_view()),
# url(r'^api/musicians/(?P<pk>\d+)/$', MusicianView.as_view()),
# url(r'^api/albums/$', AlbumListView.as_view()),
# url(r'^api/albums/(?P<pk>\d+)/$', AlbumView.as_view()),