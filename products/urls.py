from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_information, name='product_information'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('confirm_delete_product/<int:product_id>', views.confirm_delete_product, name="confirm_delete_product"),
    path(
        'editcomment/<int:comment_id>',
        views.edit_comment, name='editcomment'
        ),
    path(
        "confirm_deletecomment/<int:comment_id>",
        views.delete_comment, name="confirm_deletecomment"
        ),
]