from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("books_list/", views.books_list, name="books_list"),
    path("book_detail/<int:book_id>/", views.book_detail, name="book_detail"),
    path("authors_list/", views.authors_list, name="authors_list"),
    path("book_detail/add_to_favourites/<int:book_id>/", views.add_to_favourites, name="add_to_favorites")
]