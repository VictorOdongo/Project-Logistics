from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages, auth
from user.models import Personal


def home_view(request):
    return render(request, 'home.html')

def getstarted_view(request):
    return render(request, 'user/getstarted.html')

def personal_view(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'email already exists!')
            return redirect('personal_view/')
        elif User.objects.filter(id=id).exists():
            messages.info(request, 'id number already exists!')
            return redirect('personal_view/')
        else:
            user = User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            mobile=mobile,
            email=email,
            password=password
        )
            user.save()
            
            user_model = User.objects.get
            new_profile = Personal.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            return redirect('sender-login/')
    
    
    else: 
        
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
