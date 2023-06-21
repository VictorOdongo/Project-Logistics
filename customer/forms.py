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
        
class JobCreateStep2Form(forms.ModelForm):
    pickup_address = forms.CharField(required=True)
    pickup_name = forms.CharField(required=True)
    pickup_phone = forms.CharField(required=True)

    class Meta:
        model = Job
        fields = ('pickup_address', 'pickup_lat', 'pickup_lng', 'pickup_name', 'pickup_phone')
        
class JobCreateStep3Form(forms.ModelForm):
    delivery_address = forms.CharField(required=True)
    delivery_name = forms.CharField(required=True)
    delivery_phone = forms.CharField(required=True)

    class Meta:
        model = Job
        fields = ('delivery_address', 'delivery_lat', 'delivery_lng', 'delivery_name', 'delivery_phone')
        