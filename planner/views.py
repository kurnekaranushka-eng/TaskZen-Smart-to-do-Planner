from django.shortcuts import render,redirect, get_object_or_404
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = 'home'

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'tasks': tasks})

@login_required
def task_list(request):

    category = request.GET.get('category')

    tasks = Task.objects.filter(user=request.user)

    if category:
        tasks = tasks.filter(category=category)

    # 🔥 ADD STATISTICS HERE
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='Completed').count()
    pending_tasks = tasks.filter(status='Pending').count()
    overdue_tasks = [t for t in tasks if t.is_overdue]

    # Optional: Productivity %
    if total_tasks > 0:
        productivity = (completed_tasks / total_tasks) * 100
    else:
        productivity = 0

    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'overdue_tasks': len(overdue_tasks),
        'productivity': round(productivity, 2),
    })

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form})

@login_required
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.status = 'Completed'
    task.save()
    return redirect('task_list')


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('task_list')