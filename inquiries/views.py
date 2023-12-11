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

    """
    This view allows user to submit an inquiry
    and to display all user inquiries.
    """
    inquiries = Inquiry.objects.filter(user=request.user)
    inquiries = inquiries.order_by('-created_on')

    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.user = request.user
            inquiry.save()
            message_text = 'Your inquiry was submitted successfully.'
            messages.success(request, message_text)
            return redirect(request.path)
    else:
        form = InquiryForm()

    context = {
        'form': form,
        'inquiries': inquiries,
        'base_message': True
    }
    return render(request, 'inquiries/inquiries.html', context)


@login_required
def inquiry_details(request, inquiry_id):
    """
    This view displays the inquiry details and
    allows user to add an update/reply
    to the same inquiry.
    The view checks if the users is the
    owner of the inquiry
    """

    inquiry = get_object_or_404(Inquiry, pk=inquiry_id)

    if request.user != inquiry.user:
        messages.error(
                    request,
                    "You don't have permission to access this inquiry.")
        return redirect('home')

    # Split user_reply into a list of replies
    user_replies = inquiry.user_reply.split('\n') if inquiry.user_reply else []

    if request.method == 'POST':
        user_reply_form = UserReplyForm(request.POST)
        if user_reply_form.is_valid():
            new_reply = user_reply_form.cleaned_data['user_reply']
            user_name = request.user.username
            user_replies.append(f"{user_name}: {new_reply}")
            inquiry.user_reply = '\n'.join(user_replies)
            inquiry.save()

            messages.success(request, 'Your reply was submitted successfully.')
            return redirect('inquiry', inquiry_id=inquiry.id)
    else:
        user_reply_form = UserReplyForm()

    return render(request, 'inquiries/inquiry_details.html', {
        'inquiry': inquiry,
        'user_replies': user_replies,
        'user_reply_form': user_reply_form,
        'base_message': True
    })


@login_required
def delete_inquiry(request, inquiry_id):
    """
    This deletes the inquiry.
    The view checks if the users is the
    owner of the inquiry
    """
    inquiry = get_object_or_404(Inquiry, pk=inquiry_id)

    if request.user != inquiry.user:
        messages.error(
                    request,
                    "You don't have permission to access this inquiry.")
        return redirect('home')

    if request.method == 'POST':
        inquiry.delete()
        messages.success(
                request,
                'You have deleted the inquiry successfully.'
            )
        return redirect('home')

    context = {
        'inquiry': inquiry,
        'base_message': True
    }

    return render(request, 'inquiries/inquiry_confirm_delete.html', context)
