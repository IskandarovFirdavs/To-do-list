from django.urls import path
from books.views import template_view, book_details

app_name = 'books'

urlpatterns = [
    path('', template_view, name='list'),
    path('<int:pk>/', book_details, name='book_detail'),
]
