from django.contrib import admin
from .models import Inquiry
# Register your models here.

@admin.register(Inquiry)
class FavoritesAdmin(admin.ModelAdmin):
    """
    This class allows admin to manage inquiries on the admin panel.
    """
    list_display = ('user',
                    'created_on', 'subject', 'order_number_inquiry')
    search_fields = ['subject', 'user_message', 'user_reply', 'admin_reply']
    ordering =('created_on',)