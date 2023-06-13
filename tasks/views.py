# from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Task

def index(request):
    if request.method == 'POST':
        name = request.POST.get('task_name')
        task = Task(name=name)
        task.save()
        return redirect('index')
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'signin.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        category = request.POST.get('category')
        task = Task.objects.get(id=task_id)
        task.category = category
        task.user = request.user
        task.save()
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'tasks': tasks})
