from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User, auth
from django.contrib import messages
from user.models import Personal, Entreprise, Driver
from .models import User


def home_view(request):
    return render(request, 'home.html')

def getstarted_view(request):
    return render(request, 'user/getstarted.html')

def personal_view(request):
    if request.method == 'POST':
        u_name = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'email already exists!')
            return redirect('personal-signup')
        elif User.objects.filter(username=u_name).exists():
            messages.info(request, 'username taken!')
            return redirect('personal-signup')
        
        else:
            user = User.objects.create_user(
            username=u_name,
            email=email,
            password=password
        )
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            
            user_model = User.objects.get(username=u_name)
            new_profile = Personal.objects.create(user=user_model)
            new_profile.save()
            return redirect('sender-login')
        
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
    if request.method == 'POST':
        bizname = request.POST['bizname']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']


        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'email already exists!')
            return redirect('personal-signup')
        elif User.objects.filter(username=bizname).exists():
            messages.info(request, 'business name taken!')
            return redirect('personal-signup')
        
        else:
            user = User.objects.create_user(
            username=bizname,
            email=email,
            password=password
        )
            user.first_name = firstname
            user.last_name = lastname
            user.mobile = mobile
            user.save()
            
            user_model = User.objects.get(username=bizname)
            new_profile = Personal.objects.create(user=user_model)
            new_profile.save()
            return redirect('sender-login')
        
    else:
         return render(request, 'user/entreprise-signup.html')



def driver_view(request):
    return render(request, 'user/driver-signup.html')

def drive_view(request):
    return render(request, 'user/driver-login.html')


def sendgig_view(request):
    return render(request, 'user/sendgig.html')

def drivegig_view(request):
    return render(request, 'user/drivegig.html')

        
        
