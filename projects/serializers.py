from rest_framework import serializers
from .models import Project
class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model=Project
       fields='__all__'
       