from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from user.models import *

@login_required(login_url="/driver-login/")
def drivegig_view(request):
    return render(request, 'driver/drivegig.html', {
        "GOOGLE_MAP_API_KEY": settings.GOOGLE_MAP_API_KEY,
    })

