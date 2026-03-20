from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
<<<<<<< HEAD
=======
from datetime import date, timedelta
>>>>>>> a5c2a1c (Updated project files)


class Task(models.Model):

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

<<<<<<< HEAD
    # Category Choices
=======
>>>>>>> a5c2a1c (Updated project files)
    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Study', 'Study'),
        ('Personal', 'Personal'),
        ('Health', 'Health'),
<<<<<<< HEAD
=======
        ('Finance', 'Finance'),
        ('Other', 'Other'),
>>>>>>> a5c2a1c (Updated project files)
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Work')

<<<<<<< HEAD
    category = models.CharField(   # ✅ MOVED INSIDE CLASS
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Work'
    )

    deadline = models.DateField()
=======
    deadline = models.DateField(null=True, blank=True)
>>>>>>> a5c2a1c (Updated project files)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'
    )

<<<<<<< HEAD
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
>>>>>>> a5c2a1c (Updated project files)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

<<<<<<< HEAD
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
=======
    def __str__(self):
        return self.title

    @property
    def is_overdue(self):
        if self.deadline is None:
            return False
        return self.deadline < timezone.now().date() and self.status == 'Pending'
    
    @property
    def is_due_soon(self):
       today = date.today()
       return (
        self.status == 'Pending'
        and today <= self.deadline <= today + timedelta(days=2)
    )
>>>>>>> a5c2a1c (Updated project files)
