from django.urls import path
from . import views

urlpatterns = [
    path('add_to_favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorites/', views.favorites_page, name='favorites'),
]