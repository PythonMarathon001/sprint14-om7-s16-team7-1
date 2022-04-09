from django.urls import path
from . import views_author, views_book


urlpatterns = [
    path('author/', views_author.ApiAuthors.as_view()),
    path('author/<int:pk>/', views_author.ApiAuthorPK.as_view()),
    path('book/', views_book.ApiBooks.as_view()),
    path('book/<int:pk>/', views_book.ApiBookPK.as_view()),
]
