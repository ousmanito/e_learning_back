from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.forms import DateTimeField

class Category(models.Model):
    title = models.CharField(max_length=72, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="category", default=1)
    def __str__(self) -> str:
        return self.title

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', default=1)
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    time = models.TimeField(null = True,blank = True)
    completed = models.BooleanField(default=False)
    key = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="NULL")
    def __str__(self):
        return self.title

