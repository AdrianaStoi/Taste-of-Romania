from django.shortcuts import render, redirect, get_object_or_404
from .models import Favorites, Product

def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite, created = Favorites.objects.get_or_create(user=request.user, product=product)
    favorite.mark_as_favorite()

    favorite_count = Favorites.objects.filter(user=request.user, is_favorite=True).count()
    is_favorite = False

    if request.user.is_authenticated:
        is_favorite = product.favorites_set.filter(user=request.user, is_favorite=True).exists()

    context = {
        'is_favorite': is_favorite,
        'product': product, 
        'favorite_count':favorite_count
    }

    return render(request, 'products/product_information.html', context)

def favorites_page(request):
    favorites = Favorites.objects.filter(user=request.user, is_favorite=True)

    context = {
        'favorites': favorites
    }

    return render(request, 'favorites.html', context)