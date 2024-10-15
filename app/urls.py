from django.urls import path
from .views import AuthorViewSet, BookViewSet
urlpatterns = [
    path('authors/', AuthorViewSet.as_view(), name='authors'),
    path('books/', BookViewSet.as_view(), name='books'),
]