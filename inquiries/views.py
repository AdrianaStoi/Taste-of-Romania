from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Inquiry
from .forms import InquiryForm, UserReplyForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse


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

@login_required
def inquiry_details(request, inquiry_id):
    """ 
    This view allows user to submit an update and reply
    to the same inquiry.
    """
    inquiry = get_object_or_404(Inquiry, pk=inquiry_id)
    user_replies = None

    if request.method == 'POST':
        user_reply_form = UserReplyForm(request.POST, instance=user_replies)
        if user_reply_form.is_valid():
            new_reply = user_reply_form.cleaned_data['user_reply']
            user_name = request.user.username

            if inquiry.user_reply is None:
                inquiry.user_reply += f"\n{user_name} {timezone.now()}: {new_reply}"

            inquiry.save()
            messages.success(request, 'Your reply was submitted successfully.')
            return HttpResponseRedirect(reverse('inquiry', args=[inquiry_id]))
    else:
        user_reply_form = UserReplyForm()

    # Splits user_reply into a list of lines
    user_replies = inquiry.user_reply.split('\n') if inquiry.user_reply else []

    return render(request, 'inquiries/inquiry_details.html', {
        'inquiry': inquiry,
        'user_replies': user_replies,
        'user_reply_form': user_reply_form,
    })
