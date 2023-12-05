from django.urls import path
from . import views

urlpatterns = [
    path('addtofavorites/<int:product_id>/', views.AddtoFavorites.as_view(), name='addtofavorites'),
    path('favorites/', views.FavoritesPage.as_view(), name='favorites'),
]
