import datetime
from enum import unique
from django.shortcuts import render
from .models import Book

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order


def order_list(request):
    context = {'order_list': Order.objects.all()}
    return render(request, 'order/order_list.html', context)


def not_returned_books(request):
    user_info = Order.get_not_returned_books
    context = {'not_returned_books': user_info}
    return render(request, 'order/not_returned_books.html', context)

