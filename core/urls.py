from django.urls import path, include 
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BorrowBookView, ReturnBookView, MyBooksView, home_view, BookAPIViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookAPIViewSet, basename='books')

urlpatterns = [
    path('', home_view, name='home'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/new/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/borrow/', BorrowBookView.as_view(), name='borrow_book'),
    path('book/<int:pk>/return/', ReturnBookView.as_view(), name='return_book'),
    path('my-books/', MyBooksView.as_view(), name='my_books'),
    path('api/', include(router.urls)),
]