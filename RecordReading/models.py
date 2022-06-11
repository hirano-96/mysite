from tabnanny import verbose
from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "作者")
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "タイトル")
    author = models.ForeignKey(Author, on_delete = models.CASCADE, verbose_name = "作者", related_name = "book")
    def __str__(self):
        return self.title

class Memory(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE, verbose_name = "タイトル", related_name = "memory")
    start_date = models.DateField()
    end_date = models.DateField()
    memory = models.TextField
    def __str__(self):
        return self.memory