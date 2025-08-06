from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Book, User
from .forms import BookForm

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer

def home_view(request):
    return render(request, 'home.html')
    
class BookListView(ListView):
    model = Book
    template_name = 'core/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'core/book_detail.html'
    context_object_name = 'book'

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == 'administrator'

class BookCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'core/book_form.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'core/book_form.html'
    success_url = reverse_lazy('book_list')

class RegularUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == 'regular_user'

class BorrowBookView(LoginRequiredMixin, RegularUserRequiredMixin, UpdateView):
    model = Book
    fields = []
    template_name = 'core/borrow_book.html'
    success_url = reverse_lazy('my_books')

    def form_valid(self, form):
        book = form.instance
        if book.stock_quantity > 0:
            book.stock_quantity -= 1
            book.save()
            self.request.user.borrowed_books.add(book)
        return super().form_valid(form)

class ReturnBookView(LoginRequiredMixin, RegularUserRequiredMixin, UpdateView):
    model = Book
    fields = []
    template_name = 'core/return_book.html'
    success_url = reverse_lazy('my_books')

    def form_valid(self, form):
        book = form.instance
        if self.request.user in book.borrowed_by.all():
            book.stock_quantity += 1
            book.save()
            self.request.user.borrowed_books.remove(book)
        return super().form_valid(form)

class MyBooksView(LoginRequiredMixin, RegularUserRequiredMixin, ListView):
    model = Book
    template_name = 'core/my_books.html'
    context_object_name = 'borrowed_books'

    def get_queryset(self):
        return self.request.user.borrowed_books.all()

class BookAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAdminUser]

        return [permission() for permission in self.permission_classes]

    @action(detail=True, methods=['post'])
    def borrow(self, request, pk=None):
        book = self.get_object()
        user = request.user
        
        if not user.is_authenticated or user.role != 'regular_user' or book.stock_quantity <= 0:
            return Response({'error': 'You do not have permissions or the book is not available.'}, status=status.HTTP_400_BAD_REQUEST)
        
        book.stock_quantity -= 1
        book.save()
        user.borrowed_books.add(book)
        
        return Response({'status': 'Book borrowed successfully.'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        book = self.get_object()
        user = request.user
        
        if not user.is_authenticated or user.role != 'regular_user' or not user.borrowed_books.filter(pk=book.pk).exists():
            return Response({'error': 'You have not borrowed this book.'}, status=status.HTTP_400_BAD_REQUEST)
        
        book.stock_quantity += 1
        book.save()
        user.borrowed_books.remove(book)
        
        return Response({'status': 'Book returned successfully.'}, status=status.HTTP_200_OK)