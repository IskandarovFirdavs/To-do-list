from django.urls import path
from books.views import template_view, book_detail, book_details

app_name = 'books'

urlpatterns = [
    path('', template_view, name='list'),
    path('detail/', book_detail, name='detail'),
    path('books/<int:books_id>/', book_details, name='book_detail'),
]