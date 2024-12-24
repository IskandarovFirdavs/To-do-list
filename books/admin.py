from django.contrib import admin
from .models import Books


class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'image')


admin.site.register(Books, BooksAdmin)
