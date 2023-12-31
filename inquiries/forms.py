from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'phone_number',
                  'subject', 'order_number_inquiry', 'user_message'
                  ]
    order_number_inquiry = forms.CharField(
        label='Order Number',
        required=False
    )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'subject': 'Subject',
        }


class UserReplyForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['user_reply']

    user_reply = forms.CharField(
        label='Reply',
        required=True,
        widget=forms.Textarea
    )
