from django.shortcuts import render, get_object_or_404
from .models import Books


def template_view(request):
    books = Books.objects.all()
    return render(request, 'index.html', {'books' : books})

def book_detail(request):
    return render(request, 'detail.html')

def book_details(request, books_id):
    books = get_object_or_404(Books, id=books_id)
    return render(request, 'detail.html', {'books' : books})

