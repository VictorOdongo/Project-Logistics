from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User, auth
from django.contrib import messages
from user.models import Personal
from .models import User


def home_view(request):
    return render(request, 'home.html')

def getstarted_view(request):
    return render(request, 'user/getstarted.html')

def personal_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        lastname = request.POST['lastname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'email already exists!')
            return redirect('personal_view')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'username taken!')
            return redirect('personal_view')
        
        else:
            user = User.objects.create_user(
            username=username,
            lastname=lastname,
            mobile=mobile,
            email=email,
            password=password
        )
            user.save()
            
            user_model = User.objects.get(username=username)
            new_profile = Personal.objects.create(user=user_model, username=username)
            new_profile.save()
            return redirect('sender-login/')
    
    
    else: 
        
        return render(request, 'user/personal-signup.html')
    
    
def send_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.send_view(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid login details')
            return redirect('sender-login')
        
    return render(request, 'user/sender-login.html')

def logout(request):
    auth.logout(request)
    return render('/')


    
           
def business_view(request):
    return render(request, 'user/entreprise-signup.html')

def driver_view(request):
    return render(request, 'user/driver-signup.html')

def drive_view(request):
    return render(request, 'user/driver-login.html')


def sendgig_view(request):
    return render(request, 'user/sendgig.html')

def drivegig_view(request):
    return render(request, 'user/drivegig.html')

        
        
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
