from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Prefetch

from .models import Category, Book, Comment
from .serializers import CategorySerializer, BookSerializer, CommentSerializer,BookListSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.action =='list':
            return Category.objects.only('id','name')
        return Category.objects.all()


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category','is_active']
    search_fields = ['title','author', 'description']
    ordering_fields = ['price','title']

    def get_queryset(self):
        if self.action=='list':
            return (
                Book.objects.select_related('category').only('id', 'title','author','price', 'is_active','category__id','category__name',)
            )
        return (
            Book.objects.select_related('category').prefetch_related(Prefetch('comments',queryset=Comment.objects.only('id', 'name', 'text', 'rating', 'book_id').order_by('-created_at'),))
        )

    def get_serializer_class(self):
        if self.action =='list':
            return BookListSerializer
        return BookSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.action=='list':
            return (Comment.objects.select_related('book__category').defer('text','book__description').order_by('-created_at'))
        return Comment.objects.select_related('book__category')


    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['book','rating']
    search_fields = ['name', 'text','book__title']
    ordering_fields = ['rating', 'created_at']