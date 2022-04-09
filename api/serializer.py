from rest_framework import serializers
from author.models import Author
from book.models import Book
from order.models import Order
from authentication.models import CustomUser


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'surname', 'patronymic')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'count', 'authors')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'book', 'created_at', 'end_at', 'plated_end_at')


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'email', 'password',
                  'updated_at', 'created_at', 'role', 'is_active')
