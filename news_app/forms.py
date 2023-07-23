from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=150)
#     email = forms.EmailField(max_length=150)
#     message = forms.CharField()