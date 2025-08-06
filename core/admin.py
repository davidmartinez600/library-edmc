from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, User

# Personalización del admin para el usuario, agregando el campo "role"
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

# Configuración básica del admin para el modelo Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'stock_quantity')