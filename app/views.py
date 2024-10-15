from rest_framework import viewsets

from app.models import Author, Book
from app.serializers import AuthorSerializer, BookSerializer
from app.filters import AuthorFilter, BookFilter


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
