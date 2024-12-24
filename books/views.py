from django.shortcuts import render
from .models import Books


def template_view(request):
    books = Books.objects.all()
    return render(request, 'index.html', {'books' : books})

def book_detail(request):
    return render(request, 'detail.html')
