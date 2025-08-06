from django.db import models
from django.contrib.auth.models import AbstractUser

# Usuario personalizado que incluye un campo de rol
class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=[('administrator', 'Administrator'), ('regular_user', 'Regular User')],
        default='regular_user'
    )
    
    def __str__(self):
        return self.username

# Modelo de libro con información básica y relación muchos a muchos con usuarios
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    stock_quantity = models.PositiveIntegerField(default=1)
    borrowed_by = models.ManyToManyField(
        User,
        related_name='borrowed_books',
        blank=True  # Permite que un libro no esté prestado a ningún usuario
    )
    
    def __str__(self):
        return self.title
