from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from . import forms
import urllib.parse

from author.models import Author
from book.models import Book
from order.models import Order
from .forms import SearchForm


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
    context = {
        "title": f"Order by {param}({sorting})",
        "header_of_page": f"show information about all books "
                          f"sorted by {param} ({sorting})",
    }

    if param != 'order':
        if sorting == "desc":
            all_books = Book.objects.all().order_by(param).reverse()
        else:
            all_books = Book.objects.all().order_by(param)
        context['all_books'] = all_books
        return render(request, 'book/sort.html', context)
    else:
        if sorting == "desc":
            orders = Order.objects.all().order_by('pk').reverse()
        else:
            orders = Order.objects.all().order_by('pk')
        context['all_books'] = orders
        return render(request, 'book/sort_order.html', context)


# def book_filter(request):
#     if request.method == 'POST':
#         form_ = SearchForm(request.POST or None)
#         if form_.is_valid():
#             # form_data = str(request.POST["search"])
#             form_data = form_.cleaned_data.get("search")
#             # out = urllib.parse.unquote_plus(form_data)
#             # return redirect(f"http://127.0.0.1:8000/book/filter/?search={out}")
#             # return HttpResponseRedirect(f"http://127.0.0.1:8000/book/filter/?search={out}", {"out":out})
#             # return redirect(f"?search={out}")
#         # var = urllib.parse.unquote_plus(request.GET.get('search'))
#         # var = str(request.GET["search"])
#         # idsearch = request.GET
#         # return render(request, 'book/filter.html', {"context":var})
#         # return redirect(reverse('book/filter.html'), {{"context":var}})
#             try:
#                 author_id = Author.objects.filter(Q(surname__contains=form_data) |
#                                                   Q(name__contains=form_data) |
#                                                   Q(patronymic__contains=form_data))[0].id
#                 all_books = Book.objects.filter(authors__id=author_id)
#                 context = {"title": f"filter by: {form_data}",
#                            "var": form_data,
#                            "all_books": all_books,
#                            }
#                 return render(request, 'book/filter.html', context)
#                 # return redirect('book/filter.html', context)
#             except IndexError:
#                 return redirect(reverse('no_filter'), {"var": form_data})
#
# from django.db.models.functions import Upper
def view_search(request):
    context = {}
    if request.method == 'POST':
        form_ = SearchForm(request.POST)
        if form_.is_valid():
            word_search = str(form_.cleaned_data['search'])
            context["form_"] = form_
            context["word_search"] = word_search
            try:
                author_id = Author.objects.filter(Q(surname__icontains=word_search) |
                                                  Q(name__icontains=word_search) |
                                                  Q(patronymic__icontains=word_search))[0].id
                all_books = Book.objects.filter(authors__id=author_id)
                context["title"] = f"filter by: {word_search}"
                context["all_books"] = all_books
                context["table"] = 1
            except IndexError:
                context["no_match"] = "no match!"
    else:
        context["form_"] = SearchForm()
    return render(request, 'book/filter.html', context)


def no_filter(request):
    title = f"No books matching your search"
    return render(request, 'book/no_filter.html', locals())
