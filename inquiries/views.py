from django.shortcuts import render, redirect
from .models import Inquiry
from .forms import InquiryForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def user_inquiry(request):

    inquiries = Inquiry.objects.filter(user=request.user).order_by('-created_on')

    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.user = request.user
            inquiry.save()
            messages.success(request, 'Your inquiry was submitted successfully.')
            return redirect(request.path)
    else:
        form = InquiryForm()

    return render(request, 'inquiries/inquiries.html', {'form': form, 'inquiries': inquiries})
