from django.urls import path, include
from . import views


urlpatterns = [
    path('author/', views.ApiAuthors.as_view()),
    path('author/<int:pk>/', views.ApiAuthorPK.as_view()),
]
