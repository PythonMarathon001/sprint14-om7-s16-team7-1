from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from book.models import Book
from .serializer import BookSerializer


class ApiBooks(APIView):
    def get(self, request):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiBookPK(APIView):
    def get(self, request, pk):
        # book = Book.objects.get(pk=pk)
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def delete(self, request, pk):
        if Book.delete_by_id(pk):
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        book = Book.objects.get(pk=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid():
            book = serializer.save()
            return Response(f"Successful updated {book}", status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
