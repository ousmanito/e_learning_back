from rest_framework import viewsets
from todo.serializers import TaskSerializer, UserSerializer
from todo_app.models import Task
from django.contrib.auth.models import User
from rest_framework import permissions


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer