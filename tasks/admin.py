# admin.py
from django.contrib import admin
from .models import  Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'project', 'assigned_to', 'deadline')
    list_filter = ('status', 'project')
    search_fields = ('title', 'description', 'assigned_to__username')

# Register your models here.
