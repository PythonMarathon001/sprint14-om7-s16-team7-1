from django.urls import path

from . import views


urlpatterns = [
    path('all/', views.show_authors, name='show_all_authors'),
    path('add_author/', views.add_author, name='add_author'),
    path('<int:pk>/', views.edit_author, name='edit_author'),
]
