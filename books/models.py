from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.TextField()

