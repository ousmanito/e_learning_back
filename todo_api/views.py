from rest_framework import viewsets
from todo.serializers import TaskSerializer, UserSerializer
from todo_app.models import Task
from django.contrib.auth.models import User
from rest_framework import permissions


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all().filter(user = self.request.user)

    
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
