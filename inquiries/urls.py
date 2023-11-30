from django.urls import path
from . import views

urlpatterns = [
    path('inquiries/', views.user_inquiry, name='inquiries'),

]
