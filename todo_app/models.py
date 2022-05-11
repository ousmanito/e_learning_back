from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', default=1)
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null = True,blank = True)
    completed = models.BooleanField(default=False)
    key = models.AutoField(primary_key=True)
    category = models.CharField(null=True, blank=True, max_length=50)
    def __str__(self):
        return self.title
