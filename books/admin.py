from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'price', 'completed', 'created_at')  # Admin panelda ko‘rsatiladigan ustunlar
    list_filter = ('completed', 'created_at')  # Filtrlar
    search_fields = ('name', 'description', 'user__username')  # Qidirish imkoniyati
    ordering = ('-created_at',)  # Yangi ma’lumotlar oldin chiqishi uchun

