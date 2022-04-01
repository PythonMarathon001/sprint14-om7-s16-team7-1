from django.urls import path

from order import views


urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('not_returned/', views.not_returned_books, name='not_returned_books'),
    
]
