from rest_framework import serializers
from .models import Book

# Serializador para el modelo Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'