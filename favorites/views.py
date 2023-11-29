from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Favorites, Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin


class FavoritesPage(generic.ListView, LoginRequiredMixin):
    """
    This view lists favorites products.
    """
    model = Favorites
    template_name = 'favorites.html'
    context = {'favorites': Favorites.objects.all()}


class AddtoFavorites(View, LoginRequiredMixin):
    """
    This view will allow logged in users to
    add product to favorites or remove it from favorites.
    """

    def post(self, request, product_id, *args, **kwargs):
        product = get_object_or_404(Product, id=product_id)
        user = request.user

        if Favorites.objects.filter(user = user, product=product).exists():
            Favorites.objects.filter(user = user, product=product).delete()
            messages.success(
                request,
                'You have removed the product from favorites successfully.'
                )
        else:
           Favorites.objects.create(user=user,product=product, is_favorite=True)
           messages.success(
                request,
                'You have added the product to favorites successfully.'
                )
        
        favorite_count = Favorites.objects.filter(user=user, is_favorite=True).count()

        context = {
            'is_favorite': Favorites.objects.filter(user=user, product=product, is_favorite=True).exists(),
            'product': product, 
            'favorite_count':favorite_count,
        }

        return render(request, 'products/product_information.html', context)

        redirect_url = reverse('product_information', args=[product_id])
        return HttpResponseRedirect(redirect_url)
    
 