from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from user.customer import forms
from django.contrib import messages
from django.conf import settings
from user.models import *

@login_required(login_required="/driver-login/")
def drivegig(request):
    return render(request, 'customer/drivegig.html')
