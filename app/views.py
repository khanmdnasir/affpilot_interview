from rest_framework import viewsets
from rest_framework.response import Response
from app.models import Author, Book
from app.serializers import AuthorSerializer, BookSerializer
from app.filters import AuthorFilter, BookFilter
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.prefetch_related('authors').all()
    serializer_class = BookSerializer
    filterset_class = BookFilter

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        serializer = BookSerializer(self.queryset, many=True)
        return Response(serializer.data)
