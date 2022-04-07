from django.urls import path

from . import views


urlpatterns = [
    path('all/', views.index, name='books'),
    path('unordered/', views.unordered, name='unordered'),
    path('sorted/', views.book_sorted, name='sorted'),
    path('search/', views.view_search, name='view_search'),
    path('no_filter/', views.no_filter, name='no_filter'),
    path('author_id/<int:pk>/', views.all_books_author_id, name='all_books_author_id'),
    path('<int:pk>/', views.by_id, name='book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('add_book/', views.add_book, name='add_book'),
]
