from django.urls import path
from .views import AuthorViewSet, BookViewSet
urlpatterns = [
    path('authors/', AuthorViewSet.as_view({'get': 'list', 'post': 'create'}), name='authors_list_create'),
    path('authors/<int:pk>/', AuthorViewSet.as_view({'patch': 'partial_update', 'delete': 'destroy'}), name='authors_update_delete'),
    path('books/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='books_list_create'),
    path('books/<int:pk>/', BookViewSet.as_view({'patch': 'partial_update', 'delete': 'destroy'}), name='books_update_delete'),
]