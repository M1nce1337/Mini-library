from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Favourite


def index(request):
    return render(request, 'base.html')

def books_list(request):
    books = Book.objects.all()
    return render(request, 'books_list.html', {"books": books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_detail.html', {"book": book})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {"authors": authors})

def add_to_favourites(request, book_id):
    required_book = Book.objects.get(id=book_id)
    favourited_book = Favourite(book=required_book, user=request.user)
    Favourite.save(favourited_book)
    return render(request, 'favourite_added.html')