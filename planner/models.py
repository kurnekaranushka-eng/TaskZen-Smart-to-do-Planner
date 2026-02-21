from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):

    # Priority Choices
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    # Status Choices
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    # Category Choices
    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Study', 'Study'),
        ('Personal', 'Personal'),
        ('Health', 'Health'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES
    )

    category = models.CharField(   # ✅ MOVED INSIDE CLASS
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Work'
    )

    deadline = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):   # ✅ FIXED
        return self.title

    @property
    def is_overdue(self):   # ✅ MOVED INSIDE CLASS
        return self.deadline < timezone.now().date() and self.status == 'Pending'


class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title