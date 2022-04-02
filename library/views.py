from django.shortcuts import render

from author.models import Author
from book.models import Book


def custom_context(request):
    all_books = Book.objects.all()
    all_authors = Author.objects.all()
    books_id, authors_id = [], []
    for book in all_books:
        books_id.append(book.pk)
    for author in all_authors:
        authors_id.append(author.pk)
    return {"books_id": books_id,
            "authors_id": authors_id,
            "all_authors": all_authors,
            }


def index(request):
    context = {"title": "Main",
               }
    return render(request, 'index.html', context)
