import datetime
from django.shortcuts import render
from .models import Book

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order



def index(request):
    all_books = Book.objects.all()
    all_authors = Author.objects.all()
    lst_books = []
    for book in all_books:
        lst_books.append(Book.to_dict(book))
    for i in lst_books:
        tmp = []
        for k in i['authors']:
            for author in all_authors:
                if author.pk == k:
                    tmp.append(f'{author.name} {author.surname}')
        i['authors'] = tmp
    title = "all books"
    return render(request, 'book/books.html', locals())


def by_id(request, pk):
    book = Book.get_by_id(pk)
    context = {"book": book,
               "title": f"id:{pk}"
               }
    return render(request, 'book/book.html', context)


def unordered(request):
    all_books = Book.objects.all().filter(count__gt=0)
    context = {"all_books": all_books,
               "title": "unordered",
               }
    return render(request, 'book/unordered.html', context)


def all_books_author_id(request, pk):
    books_author_id = list(Book.objects.all().filter(authors__id=pk))
    context = {"books_author_id": books_author_id,
               "title": f"Author id: {pk}",
               "id": f"{pk}"
               }
    return render(request, 'book/books_auth_id.html', context)
