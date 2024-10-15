import django_filters
from app.models import Author, Book


class AuthorFilter(django_filters.FilterSet):
    class Meta:
        model = Author
        fields = ['name', 'date_of_birth']


class BookFilter(django_filters.FilterSet):
    published_date__gt = django_filters.DateFilter(field_name='published_date', lookup_expr='gte')
    published_date__lt = django_filters.DateFilter(field_name='published_date', lookup_expr='lte')
    class Meta:
        model = Book
        fields = ['title', 'genre']
