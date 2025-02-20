from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm
from django.shortcuts import get_object_or_404
from users.models import UserModel

@login_required
def index(request):
    user = get_object_or_404(UserModel, username=request.user.username)
    all_tasks = user.tasks.order_by('-pk')

    paginator = Paginator(all_tasks, 5)  
    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)

    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")  

        if price:
            price = float(price)  

        Todo.objects.create(user=user, name=name, price=price, description=description, completed=False)
        return redirect("index")

    return render(request, 'index.html', {'tasks': tasks})




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

