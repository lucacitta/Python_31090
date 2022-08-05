from django.contrib import admin
from products.models import Products

@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'is_active']