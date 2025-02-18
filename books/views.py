from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

@login_required
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")  

        if price:
            price = float(price)  

        Todo.objects.create(name=name, price=price, description=description, completed=False)
        return redirect("index")

    todos = Todo.objects.all()
    return render(request, "index.html", {"todos": todos})



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

