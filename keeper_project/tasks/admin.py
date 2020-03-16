from django.contrib import admin

# Register your models here.
from .models import Task,TaskList

admin.site.register([Task,TaskList])
