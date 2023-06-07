from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required()
def sendgig_view(request):
    return render(request, 'customer/sendgig.html')