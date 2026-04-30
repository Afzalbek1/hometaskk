from rest_framework import serializers
from .models import Category, Book, Comment


class CategorySerializer(serializers.ModelSerializer):
    url =serializers.HyperlinkedIdentityField(view_name='categories-detail')

    class Meta:
        model = Category
        fields = ['id','url','name','description']


class CommentShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','name','text','rating']

class BookListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price', 'is_active', 'category_name']




class BookSerializer(serializers.ModelSerializer):
    
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_string = serializers.StringRelatedField(source='category',read_only=True)

    category_url = serializers.HyperlinkedRelatedField(source='category',view_name='categories-detail',read_only=True)

    category_name = serializers.SlugRelatedField(source='category',slug_field='name',read_only=True)

    url = serializers.HyperlinkedIdentityField(view_name='books-detail')

    comments = CommentShortSerializer(many=True,read_only=True)

    comment_count = serializers.IntegerField(source='comments.count',read_only=True)

    class Meta:
        model = Book
        fields =[
            'id','url','category','category_string','category_url','category_name','title','author','description','price','is_active','comments','comment_count',
        ]


class CommentSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    book_string = serializers.StringRelatedField(source='book',read_only=True)

    book_url = serializers.HyperlinkedRelatedField(source='book',view_name='books-detail',read_only=True)

    book_title = serializers.SlugRelatedField(source='book',slug_field='title',read_only=True)

    url = serializers.HyperlinkedIdentityField(view_name='comments-detail')

    class Meta:
        model= Comment
        fields = [
            'id','url','book','book_string','book_url','book_title','name','text','rating','created_at',
        ]