from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Favorites(models.Model):
    """Model for Favorites"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)

    def mark_as_favorite(self):
        self.is_favorite = not self.is_favorite
        self.save()