from django import forms
from user.models import Personal, Entreprise
from django.contrib.auth.models import User

class BasicUserForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields = ('first_name', 'last_name')
        
class BasicCustomerForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ('avatar',)
        
# class BasicCustomerForm(forms.ModelForm):
#     class Meta:
#         model = Entreprise
#         fields = ('avatar',)