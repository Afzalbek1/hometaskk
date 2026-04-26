from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    
class Comment(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=150)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.book.title}"