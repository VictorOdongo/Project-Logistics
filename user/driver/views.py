from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required()
def drivegig(request):
    return render(request, 'customer/drivegig.html')