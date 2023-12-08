from django.contrib import admin
from .models import Favorites
# Register your models here.


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    """
    This class allows admin to manage favorites on the admin panel.
    """
    list_display = ('product', 'user',
                    'created_on')
