from django.urls import path

from . import views


urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('add/', views.add_order, name='add_order'),
    path('edit/<int:pk>', views.edit_order, name='edit_order'),
    path('user_id/<int:pk>', views.order_by_user_id, name='order_user_id'),
    path('not_returned/', views.not_returned_books, name='not_returned_books'),
]
