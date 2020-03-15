from django.contrib import admin

# Register your models here.
from .models import Task,TaskList

my_models=[Task,TaskList]
admin.site.register(my_models)
