from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.second_name

class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books", null=True)
    pub_date = models.DateField("date published")
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourited_by", null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="favourites", null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.name