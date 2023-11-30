from django.urls import path
from . import views

urlpatterns = [
    path('inquiries/', views.user_inquiry, name='inquiries'),
    path('inquiry/<int:inquiry_id>/', views.inquiry_details, name='inquiry'),
]
