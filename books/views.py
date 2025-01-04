from django.shortcuts import render, get_object_or_404
from .models import BookModel, AuthorModel




def template_view(request):
    books = BookModel.objects.order_by('-pk')
    context = {
        'books': books
    }
    return render(request, 'index.html', context)


def book_details(request, pk):
    book = get_object_or_404(BookModel, pk=pk)
    context = {
        'book': book
    }
    return render(request, 'detail.html', context)
