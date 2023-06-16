from django import forms
from user.models import Personal
from django.contrib.auth.models import User
from customer.models import Job

class BasicUserForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields = ('first_name', 'last_name')
        
class BasicCustomerForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ('avatar',)
        
class JobCreateStep1Form(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('name', 'description', 'category', 'size', 'quantity', 'photo')
        