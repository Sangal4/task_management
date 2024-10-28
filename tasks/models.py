from django.db import models
from projects.models import Project
from django.conf import settings
# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=400)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='Pending')
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='tasks')
    assigned_to=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='assigned_tasks'
    )
    deadline=models.DateField()
    
    def __str__(self):
        return f"{self.title}-{self.status}"
    
    