from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=[('administrator', 'Administrator'), ('regular_user', 'Regular User')], default='regular_user')
    
    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    stock_quantity = models.PositiveIntegerField(default=1)
    borrowed_by = models.ManyToManyField(User, related_name='borrowed_books', blank=True)
    
    def __str__(self):
        return self.title