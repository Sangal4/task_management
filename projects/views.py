from django.shortcuts import render
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectsSerializer
# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectsSerializer
    