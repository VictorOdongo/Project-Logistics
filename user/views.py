from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def home_view(request):
    return render(request, 'home.html')

def getstarted_view(request):
    return render(request, 'user/getstarted.html')

def personal_view(request):
    return render(request, 'user/personal-signup.html')

def business_view(request):
    return render(request, 'user/entreprise-signup.html')

def driver_view(request):
    return render(request, 'user/driver-signup.html')

def drive_view(request):
    return render(request, 'user/driver-login.html')

def send_view(request):
    return render(request, 'user/sender-login.html')

def sendgig_view(request):
    return render(request, 'user/sendgig.html')

def drivegig_view(request):
    return render(request, 'user/drivegig.html')



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your desired page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to your desired page
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
