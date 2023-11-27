from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    This class allows admin to manage products on the admin panel.
    """
    list_display = ('name', 'sku', 'category','price','slug', 
                    'created_on', 'image')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created_on', 'category')
    search_fields = ['name', 'description', 'category']
    ordering =('sku',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    This class allows admin to manage Category on the admin panel.
    It displays the category name, creation date and update date.
    """
    list_display = ('friendly_name', 'name','created_on', 'updated_on')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    This class allows admin to manage reviews on the admin panel.
    """
    list_display = ('product', 'user', 'comment', 'rating',
                    'created_on', 'updated_on')
    list_filter = ('created_on', 'product')
    search_fields = ('user', 'comment', 'product')