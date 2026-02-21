from django.contrib import admin
from .models import Task, SubTask


class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'category', 'status', 'deadline')
    list_filter = ('priority', 'status', 'category')
    search_fields = ('title', 'user__username')
    ordering = ('-created_at',)
    inlines = [SubTaskInline]


admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask)