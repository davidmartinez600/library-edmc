from django.urls import path, include
from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView,
    BorrowBookView, ReturnBookView, MyBooksView, home_view, BookAPIViewSet
)
from rest_framework.routers import DefaultRouter

# Router para la API REST
router = DefaultRouter()
router.register(r'books', BookAPIViewSet, basename='books')

urlpatterns = [
    path('', home_view, name='home'),  # Página principal
    path('books/', BookListView.as_view(), name='book_list'),  # Lista de libros
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # Detalle libro
    path('book/new/', BookCreateView.as_view(), name='book_create'),  # Crear libro (admin)
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),  # Editar libro (admin)
    path('book/<int:pk>/borrow/', BorrowBookView.as_view(), name='borrow_book'),  # Pedir libro (usuario)
    path('book/<int:pk>/return/', ReturnBookView.as_view(), name='return_book'),  # Devolver libro (usuario)
    path('my-books/', MyBooksView.as_view(), name='my_books'),  # Libros prestados por el usuario
    path('api/', include(router.urls)),  # Endpoints API REST
]