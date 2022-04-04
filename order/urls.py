from django.urls import path

from . import views


urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('user_id/<int:pk>', views.order_by_user_id, name='order_user_id'),
    path('not_returned/', views.not_returned_books, name='not_returned_books'),
]
