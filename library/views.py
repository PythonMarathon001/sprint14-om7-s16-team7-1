from django.shortcuts import render

from author.models import Author
from authentication.models import CustomUser
from book.models import Book


def custom_context(request):
    all_books = Book.objects.all()
    all_authors = Author.objects.all()
    all_users = CustomUser.objects.all()

    books_id, authors_id, users_id = [], [], []
    for book in all_books:
        books_id.append(book.pk)
    for author in all_authors:
        authors_id.append(author.pk)
    for user in all_users:
        users_id.append(user.pk)
    return {"books_id": books_id,
            "authors_id": authors_id,
            "users_id": users_id,
            "all_authors": all_authors,
            }


def index(request):
    context = {"title": "Main",
               }
    return render(request, 'index.html', context)
