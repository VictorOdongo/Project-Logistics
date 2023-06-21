# import requests
# import stripe
# import firebase_admin

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from customer import forms
from django.contrib import messages 
from django.conf import settings
from customer.models import *

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
        customer_form = forms.BasicCustomerForm(request.POST, request.FILES, instance=request.user)
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

                messages.success(request, 'Your profile has been updated')
                return redirect(reverse('customer:profile'))

        elif request.POST.get('action') == 'update_password':
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)

                messages.success(request, 'Your password has been updated')
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
    current_customer =request.user.personal
    
    creating_job = Job.objects.filter(customer=current_customer, status=Job.CREATING_STATUS).last()
    step1_form = forms.JobCreateStep1Form(instance=creating_job)
    step2_form = forms.JobCreateStep2Form(instance=creating_job)
    # step3_form = forms.JobCreateStep3Form(instance=creating_job)

    
    if request.method == "POST":
        if request.POST.get('step') == '1':
            step1_form = forms.JobCreateStep1Form(request.POST, request.FILES, instance=creating_job)
            if step1_form.is_valid():
                creating_job = step1_form.save(commit=False)
                creating_job.customer = current_customer
                creating_job.save()
                return redirect(reverse('customer:create_gig'))
            
        elif request.POST.get('step') == '2':
            step2_form = forms.JobCreateStep2Form(request.POST, instance=creating_job)
            if step2_form.is_valid():
                creating_job = step2_form.save()
                return redirect(reverse('customer:create_gig'))
            
        elif request.POST.get('step') == '3':
            step3_form = forms.JobCreateStep3Form(request.POST, instance=creating_job)
            if step3_form.is_valid():
                creating_job = step3_form.save()

                # try:
                #     r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&mode=transit&key={}".format(
                #     creating_job.pickup_address,
                #     creating_job.delivery_address,
                #     settings.GOOGLE_MAP_API_KEY,
                # ))
                #     print(r.json()['rows'])
                    
                #     distance = r.json()['rows'][0]['elements'][0]['distance']['value']
                #     duration = r.json()['rows'][0]['elements'][0]['duration']['value']
                #     creating_job.distance = round(distance / 1000, 2)
                #     creating_job.duration = int(duration / 60)
                #     creating_job.price = creating_job.distance * 1  # $1 per Km
                #     creating_job.save()
                                         
                # except Exception as e:
                #     print(e)
                #     messages.error(request, "Unfortunately, we do not support deliveries at this distance.")
               
                return redirect(reverse('customer:create_gig'))
            
        # elif request.POST.get('step') == '4':
        #     if creating_job.price:
        #         try:
        #             payment_intent = stripe.PaymentIntent.create(
        #                 amount=int(creating_job.price * 100),
        #                 currency='usd',
        #                 automatic_payment_methods={"enabled": True},
        #                 customer=current_customer.stripe_customer_id,
        #                 payment_method=current_customer.stripe_payment_method_id,
        #                 off_session=True,
        #                 confirm=True,
        #             )
                    
        #             Transaction.objects.create(
        #                 stripe_payment_intent_id = payment_intent['id'],
        #                 job = creating_job,
        #                 amount = creating_job.price,
        #             )
                    
        #             creating_job.status = Job.PROCESSING_STATUS
        #             creating_job.save()
                    
        #             return redirect(reverse('customer:sendgig'))
                    
        #         except stripe.error.CardError as e:
        #             err = e.error
        #             # Error code will be authentication_required if authentication is needed
        #             print("Code is: %s" % err.code)
        #             payment_intent_id = err.payment_intent['id']
        #             payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
                                
    #Determine the current step
    if not creating_job:
        current_step = 1
    # elif creating_job.delivery_name:
    #     current_step = 4
    elif creating_job.pickup_name:
        current_step = 3
    else:
        current_step = 2
                           
    return render(request, 'customer/create_gig.html', {
        "job": creating_job,
        "step": current_step,
        "step1_form": step1_form,
        "step2_form": step2_form,
        # "step3_form": step3_form,
        # "GOOGLE_MAP_API_KEY": settings.GOOGLE_MAP_API_KEY

    })
       
       
    # Payment method 
@login_required(login_url="/sender-login/")
def payment_method(request):     
    return render(request, 'customer/payment_method.html')
                



