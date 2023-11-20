from django.contrib import admin
from .models import Product, Category

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    This class allows admin to manage products on the admin panel.
    """
    list_display = ('name', 'SKU', 'category','price','slug', 
                    'created_on')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created_on', 'name')
    search_fields = ['name', 'description', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    This class allows admin to manage Category on the admin panel.
    It displays the category name, creation date and update date.
    """
    list_display = ('name', 'created_on', 'updated_on')
