from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

@login_required
def index(request):
    if not request.user.is_authenticated:
        return redirect("login")  

    # todos = Todo.objects.filter(user=request.user)
    todos = Todo.objects.filter(user=request.user).order_by('-id')[:5]  
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user 
            todo.save()
            return redirect("index")

    context = {
        'todos': todos,
        'form': form
    }
    return render(request, 'index.html', context)


@login_required
def update(request, pk):
    todo = Todo.objects.get(id=pk)

    if todo.user != request.user:
        return redirect("index")  

    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {'todo': todo, 'form': form}
    return render(request, 'update.html', context)

@login_required
def delete(request, pk):
    todo = Todo.objects.get(id=pk)

    if todo.user != request.user:
        return redirect("index")  

    if request.method == 'POST':
        todo.delete()
        return redirect("index")

    context = {'todo': todo}
    return render(request, 'delete.html', context)

