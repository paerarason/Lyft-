from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title=models.CharField(max_length=40)
    description=models.TextField()
    deadline=models.DateField(null=True)
    def __str__(self) :
        return self.title
    class Meta:
        ordering=['deadline']  
class USER(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    tasks=models.ForeignKey(Task,on_delete=models.CASCADE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
