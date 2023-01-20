from django.contrib import admin
from applications.account.models import CustomUser
# from django import forms
# from phonenumber_field.widgets import PhoneNumberPrefixWidget

# class ContactForm(forms.ModelForm):
#     class Meta:
#         widgets = {
#             'contact': PhoneNumberPrefixWidget(initial='US'),
#         }

admin.site.register(CustomUser)
