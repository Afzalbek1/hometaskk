from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BookViewSet,CommentViewSet


router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='categories')
router.register('books', BookViewSet, basename='books')
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]