from django.contrib import admin

from .models import Category, Task, TaskCategoryModel


class TaskInline(admin.StackedInline):
    model = Category
    extra = 5


class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskInline]


admin.site.register(Category)
admin.site.register(Task)
admin.site.register(TaskCategoryModel)
