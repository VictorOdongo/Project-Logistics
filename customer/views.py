from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from customer import forms
from django.contrib import messages as message_profile
from django.conf import settings
from user.models import *

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


@login_required(login_url="/sender-login/")
def sendgig_view(request):
    return render(request, 'customer/sendgig.html')

@login_required(login_url="/sender-login/")
def profile_page(request):
    user_form = forms.BasicUserForm(instance=request.user)
    customer_form = forms.BasicCustomerForm(instance=request.user)
    password_form = PasswordChangeForm(request.user)
    
    if request.method == 'POST':
        user_form = forms.BasicUserForm(request.POST, instance=request.user)
        customer_form = forms.BasicCustomerForm(request.POST, request.FILES, instance=request.user.Personal)
        password_form = PasswordChangeForm(request.user)

    if request.method == "POST":
        if request.POST.get('action') == 'update_profile':
            user_form = forms.BasicUserForm(
                request.POST, instance=request.user)
            customer_form = forms.BasicCustomerForm(
                request.POST, request.FILES, instance=request.user)

            if user_form.is_valid() and customer_form.is_valid():
                user_form.save()
                customer_form.save()

                message_profile.success(request, 'Your profile has been updated')
                return redirect(reverse('customer:profile'))

        elif request.POST.get('action') == 'update_password':
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)

                message_profile.success(request, 'Your password has been updated')
                return redirect(reverse('customer:profile'))

        # elif request.POST.get('action') == 'update_phone':
        #     # Get Firebase user data
        #     firebase_user = auth.verify_id_token(request.POST.get('id_token'))
        #     request.user.customer.phone_number = firebase_user['phone_number']
        #     request.user.customer.save()
        #     return redirect(reverse('customer:profile'))

    return render(request, 'customer/profile.html', {
        "user_form": user_form,
        "customer_form": customer_form,
        "password_form": password_form
    })
    
    
    # Job posting
@login_required(login_url="/sender-login/")
def create_gig(request): 
    return render(request, 'customer/create_gig.html')
       
       
    # Payment method 
@login_required(login_url="/sender-login/")
def payment_method(request):     
    return render(request, 'customer/payment_method.html')
                



