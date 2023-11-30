from django.shortcuts import render, redirect, get_object_or_404
from .models import Inquiry
from .forms import InquiryForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def user_inquiry(request):

    """ This view allows user to submit an inquiry
        and to display all user inquiries.
    """
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

def inquiry_details(request, inquiry_id):

    inquiry = get_object_or_404(Inquiry, pk=inquiry_id)
    return render(request, 'inquiries/inquiry_details.html', {'inquiry': inquiry})