from django.urls import path

from books.views import template_view, book_detail

app_name = 'books'

urlpatterns = [
    path('', template_view, name='list'),
    path('detail/', book_detail, name='detail'),
]