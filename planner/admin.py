from django.contrib import admin
<<<<<<< HEAD
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
=======
from .models import Task
from django.contrib.auth.models import User


class TaskAdmin(admin.ModelAdmin):

    # Columns visible in admin list view
    list_display = (
        'title',
        'user',
        'priority',
        'category',
        'status',
        'deadline',
        'is_overdue_display',
        'created_at',
    )

    # Filters on right sidebar
    list_filter = (
        'user',
        'priority',
        'category',
        'status',
        'deadline',
        'created_at',
    )

    # Search bar
    search_fields = (
        'title',
        'description',
        'user__username',
    )

    # Default ordering (latest first)
    ordering = ('-created_at',)

    # Read-only fields
    readonly_fields = ('created_at', 'updated_at')

    # Prevent showing soft-deleted tasks
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_deleted=False)

    # Custom column to show overdue status
    def is_overdue_display(self, obj):
        return obj.is_overdue
    is_overdue_display.boolean = True
    is_overdue_display.short_description = "Overdue?"


admin.site.register(Task, TaskAdmin)

# Custom Admin Branding
admin.site.site_header = "TaskZen Administration"
admin.site.site_title = "TaskZen Admin Portal"
admin.site.index_title = "Welcome to TaskZen Admin Dashboard"
>>>>>>> a5c2a1c (Updated project files)
