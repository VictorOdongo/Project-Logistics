from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from user.customer import forms

@login_required()
def sendgig_view(request):
    return redirect(reverse('customer:profile'))

@login_required(login_url="sender-login?next=/customer/")
def profile_page(request):
    user_form = forms.BasicUserForm(instance=request.user)
    
    if request.method == 'POST':
        user_form = forms.BasicUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse('customer:profile'))

    return render(request, 'customer/profile.html', {
        "user_form": user_form,
    })