from django.contrib import admin
from todo_app import models

class TaskInline(admin.StackedInline):
    model = models.Category
    extra = 5


class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskInline]

admin.site.register(models.Category)
admin.site.register(models.Task)
admin.site.register(models.TaskCategoryModel)
