from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, on_delete=models.DO_NOTHING)
    published_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title
