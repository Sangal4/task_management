from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework import viewsets
# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer