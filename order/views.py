from django.shortcuts import render

from authentication.models import CustomUser
from order.models import Order


def order_list(request):
    sorting = request.GET.get('sorting')
    param = request.GET.get('param')

    if sorting == "desc":
        order_list = Order.objects.all().order_by(param).reverse()
    else:
        order_list = Order.objects.all().order_by(param)

    title = f"Orders by sorting:{param}({sorting})"
    context = {'order_list': order_list,
               'sorting': sorting,
               'param': param,
               "title": title,
               }
    return render(request, 'order/order_list.html', context)


def not_returned_books(request):
    user_info = Order.not_returned_on_time
    title = "doesn't hand over books on time"
    context = {'not_returned_books': user_info,
               "title": title,
               }
    return render(request, 'order/not_returned_books.html', context)


def order_by_user_id(request, pk):
    order_list = Order.objects.all().filter(user__pk=pk)
    user_name = CustomUser.get_by_id(pk)
    title = f"Order by user ID:{pk}"
    context = {"user_id": pk,
               "order_list": order_list,
               "user_name": user_name,
               "title": title,
               }
    return render(request, 'order/user_id.html', context)
