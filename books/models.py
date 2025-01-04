from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.PositiveIntegerField(),
    pseudo_name = models.CharField(max_length=30, null=True, blank=True)
    about = models.TextField()

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class BookModel(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        AuthorModel,
        on_delete=models.CASCADE,
        related_name='books'
    )
    long_description = models.TextField()
    short_description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    price = models.FloatField()
    year = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
