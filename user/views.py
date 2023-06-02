from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Personal, Entreprise, Driver


def home_view(request):
    return render(request, 'home.html')

def getstarted_view(request):
    return render(request, 'user/getstarted.html')

def personal_signup(request):
    if request.method == 'POST':
        u_name = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'email already exists!')
            return redirect('/personal-signup')
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
            
        personal = Personal.objects.create(
                user=user,
                username=u_name,
                firstname=firstname,
                lastname=lastname,
                email=email,
                password=password
            )
        user.set_password(password)
        personal.save()
        return redirect('/sender-login')
            
    else:     
        return render(request, 'user/personal-signup.html')
    
    
def sender_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/sendgig')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('user:sender-login')
    
    return render(request, 'user/sender-login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')


    
           
def entreprise_signup(request):
    if request.method == 'POST':
        bizname = request.POST['bizname']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'email already exists!')
            return redirect('entreprise-signup')
        elif User.objects.filter(username=bizname).exists():
            messages.info(request, 'business name taken!')
            return redirect('entreprise-signup')
        
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
            new_profile = Entreprise.objects.create(user=user_model)
            new_profile.save()
            return redirect('sender-login')
        
    else:
         return render(request, 'user/entreprise-signup.html')



def driver_signup(request):
    return render(request, 'user/driver-signup.html')

def drive_login(request):
    return render(request, 'user/driver-login.html')

def sendgig_view(request):
    return render(request, 'user/sendgig.html')

def drivegig_view(request):
    return render(request, 'user/drivegig.html')

        
        
