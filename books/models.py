from django.db import models
from django.conf import settings  

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
