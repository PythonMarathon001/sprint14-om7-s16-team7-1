import datetime
from django.shortcuts import render
from .models import Book

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order
import pytz


""" Create a user object to be used by the tests """


# TEST_DATE = datetime.datetime(2017, 4, 10, 12, 00, tzinfo=pytz.utc)
# TEST_DATE_END = TEST_DATE + datetime.timedelta(days=15)
# time_mock = datetime.datetime(2017, 4, 10, 12, 00, tzinfo=pytz.utc)
#     with mock.patch('django.utils.timezone.now') as mock_time:
#         mock_time.return_value = time_mock
# user = CustomUser(id=111, email='email@mail.com', password='1234', first_name='fname',
#                        middle_name='mname',
#                        last_name='lname')
# user.save()
# user_free = CustomUser(id=222, email='2email@mail.com', password='1234', first_name='2fname',
#                             middle_name='2mname',
#                             last_name='2lname')
# user_free.save()
#
# author1 = Author(id=101, name="author1", surname="s1", patronymic="p1")
# author1.save()
#
# author2 = Author(id=102, name="author2", surname="s2", patronymic="p2")
# author2.save()
#
# book1 = Book(id=101, name="book1", description="description1", count=1)
# book1.save()
# book1.authors.add(author1)
# book1.save()
#
# book2 = Book(id=102, name="book2", description="description2")
# book2.save()
# book2.authors.add(author2)
# book2.save()
#
# book3 = Book(id=103, name="book3", description="description3")
# book3.save()
# book3.authors.add(author1)
# book3.authors.add(author2)
# book3.save()
#
# order1 = Order(id=101, user=user, book=book1, plated_end_at=TEST_DATE)
# order1.save()
# order2 = Order(id=102, user=user, book=book2, plated_end_at=TEST_DATE)
# order2.save()
# order3 = Order(id=103, user=user, book=book3, end_at=TEST_DATE_END, plated_end_at=TEST_DATE)
# order3.save()

author1 = Author(id=101, name="author1", surname="s1", patronymic="p1")
author1.save()

author2 = Author(id=102, name="author2", surname="s2", patronymic="p2")
author2.save()

book1 = Book(id=101, name="book1", description="description1", count=1)
book1.save()
book1.authors.add(author1)
book1.save()

book2 = Book(id=102, name="book2", description="description2")
book2.save()
book2.authors.add(author2)
book2.save()

book3 = Book(id=103, name="book3", description="description3")
book3.save()
book3.authors.add(author1)
book3.authors.add(author2)
book3.save()


# Create your views here.

def index(request):
    all_books = Book.objects.all()
    context = {"all_books": all_books,
               }
    return render(request, 'books.html', context)


def by_id(request, pk):
    book = Book.get_by_id(pk)
    context = {"book": book,
               }
    return render(request, 'book.html', context)


# def unordered(request):
#     all_books = Book.objects.all().filter()
#     context = {"all_books": all_books,
#                }
#     return render(request, 'books.html', context)
#     pass

def all_books_author_id(request, pk):
    books_author_id = list(Book.objects.all().filter(authors__id=pk))
    context = {"books_author_id": books_author_id,
               }
    return render(request, 'books_auth_id.html', context)
