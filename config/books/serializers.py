from rest_framework import serializers
from .models import Category, Book,Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name',
        read_only=True
    )

    class Meta:
        model = Book
        fields = [
            'id','category','category_name','title','author','description','price','is_active'
        ]

    class CommentSerializer(serializers.ModelSerializer):
        book_title = serializers.CharField(
        source='book.title',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = [
            'id','book','book_title','name','text','rating','created_at',
        ]