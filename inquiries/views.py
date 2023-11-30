from django.shortcuts import render, redirect
from .models import Inquiry
from .forms import InquiryForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic



class AllInquiries(generic.ListView):
    model = Inquiry
    inquiries = Inquiry.objects.all()
    template_name = 'inquiries/inquiries.html'
    context_object_name = 'inquiries'

@login_required
def user_inquiry(request):
    inquiry = None

    if request.method == 'POST':
        form =InquiryForm(request.POST)
        if form.is_valid:
            inquiry = form.save(commit=False)
            inquiry.user = request.user
            inquiry.save()
            messages.success(request, 'Your inquiry was submitted successfully.')
            return redirect(request.path)
    else:
        form = InquiryForm()
    
    return render(request, 'inquiries/inquiries.html', {'inquiry': inquiry, 'form': form})
