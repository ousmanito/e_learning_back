from dataclasses import field
from rest_framework import serializers
from todo_app.models import Task
from django.contrib.auth.models import User
from django.db import models
from rest_framework import permissions

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['user', 'title', 'description', 'completed', 'key', 'time', 'date', 'category']


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many = True, queryset = Task.objects.all())
    class Meta:
        model = User
        fields = '__all__'