from django.urls import path

from . import views


urlpatterns = [
    path('all/', views.show_all_users, name='show_all_users'),
    path('add/', views.add_user, name='add_user'),
    path('<int:pk>/', views.edit_user, name='edit_user'),
]
