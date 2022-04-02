from django.shortcuts import render
from django.db.models import Q

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order


def index(request):
    all_books = Book.objects.all()
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
    author = Author.objects.filter(pk=pk)[0]
    context = {"books_author_id": books_author_id,
               "title": f"Author id: {pk}",
               "id": f"{pk}",
               "author": author,
               }
    return render(request, 'book/books_auth_id.html', context)


def book_sorted(request):
    sorting = request.GET.get('sorting')
    param = request.GET.get('param')

    if sorting == "desc":
        all_books = Book.objects.all().order_by(param).reverse()
    else:
        all_books = Book.objects.all().order_by(param)

    context = {
        "title": f"Order by {sorting}",
        "all_books": all_books,
        "header_of_page": f"show information about all books sorted by {param} "
                          f"({sorting})"
    }
    return render(request, 'book/sort.html', context)

from django.db.models import Q
def book_filter(request):
    var = request.GET.get('var')
    author_id = Author.objects.filter(Q(surname__contains=var) |
                                      Q(name__contains=var) |
                                      Q(patronymic__contains=var))[0].id
    all_books = Book.objects.filter(authors__id=author_id)

    context = {"title": f"filter by: {var}",
               "var": var,
               "all_books": all_books,
    }
    return render(request, 'book/filter.html', context)
