from django.contrib import admin
from .models import Category,Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'price','is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'author')