from django.db import models
from django.conf import settings
# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=400)
    start_date=models.DateField(auto_now_add=True)
    end_date=models.DateField()
    created_by=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_projects"
    )
    
    def __str__(self):
        return  self.name
    
    
