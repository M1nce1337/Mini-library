from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    biography = models.TextField(blank=True, null=True)

class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    pub_date = models.DateField("date published")
    genre = models.CharField(max_length=200)

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourited_by")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="favourites")
    added_at = models.DateTimeField(auto_now_add=True)