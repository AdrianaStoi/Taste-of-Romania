from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Favorites, Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count


class FavoritesPage(generic.ListView):
    """
    This view lists favorites products.
    """
    model = Favorites
    template_name = 'favorites.html'
    context_object_name = 'favorites'
    extra_context = {'base_message': True}
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            product_id = self.request.GET.get('product_id')
            if product_id is not None:
                return Favorites.objects.filter(product=product_id, user=self.request.user)
            else:
                return Favorites.objects.filter(user=self.request.user)
        else:
            return Favorites.objects.none()

class AddtoFavorites(View, LoginRequiredMixin):
    """
    This view allows logged in users to
    add product to favorites or remove it from favorites.
    """

    model = Product
    extra_context = {'base_message': True}
    
    def post(self, request, product_id, *args, **kwargs):
        product = get_object_or_404(Product, id=product_id)
        user = request.user

        favorites, created = Favorites.objects.get_or_create(user=user, product=product)
 
        if created or not favorites.is_favorite:
            favorites.is_favorite = True
            favorites.save()
            messages.success(
                request,
                'You have added the product to favorites successfully.'
            )
            return redirect('favorites')
        else:
            favorites.is_favorite = False
            favorites.delete()
            messages.success(
                request,
                'You have removed the product from favorites successfully.'
            )
            return redirect('favorites')
    