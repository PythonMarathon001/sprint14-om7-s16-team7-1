from django.urls import path
from . import views_author, views_book, views_order, views_user


urlpatterns = [
    path('author/', views_author.ApiAuthors.as_view()),
    path('author/<int:pk>/', views_author.ApiAuthorPK.as_view()),
    path('book/', views_book.ApiBooks.as_view()),
    path('book/<int:pk>/', views_book.ApiBookPK.as_view()),
    path('order/', views_order.ApiOrders.as_view()),
    path('order/<int:pk>/', views_order.ApiOrderPK.as_view()),
    path('user/', views_user.ApiCustomUser.as_view()),
    path('user/<int:user_pk>/order/<int:order_pk>/', views_user.ApiUserOrderPK.as_view()),
    path('user/<int:pk>/', views_user.ApiCustomUserPK.as_view()),
]
