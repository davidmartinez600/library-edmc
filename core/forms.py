from django import forms
from .models import Book

# Formulario para crear y editar libros
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'stock_quantity']
        labels = {
            'title': 'Título',
            'author': 'Autor',
            'publication_year': 'Año de Publicación',
            'stock_quantity': 'Cantidad en Stock',
        }