from django import forms

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email')