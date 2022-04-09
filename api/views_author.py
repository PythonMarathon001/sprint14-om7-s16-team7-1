from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from author.models import Author
from .serializer import AuthorSerializer


class ApiAuthors(APIView):
    def get(self, request):
        all_authors = Author.objects.all()
        serializer = AuthorSerializer(all_authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiAuthorPK(APIView):
    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def delete(self, request, pk):
        if Author.delete_by_id(pk):
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        author = Author.objects.get(pk=pk)
        data = request.data
        serializer = AuthorSerializer(instance=author, data=data, partial=True)
        if serializer.is_valid():
            author = serializer.save()
            return Response(f"Successful updated: {author}", status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
