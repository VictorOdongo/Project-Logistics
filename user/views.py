from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages, auth
from user import Personal


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



def register(request):
    if request.method == 'POST':
        # Retrieve form data
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        id = request.POST['id']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        
        # Create User object
        user = User.objects.create_user(
            username=email,
            password=password,
            first_name=firstname,
            last_name=lastname,
            email=email,
            mobile=mobile
        )
        
        user.save()
        print('Registration successful')
        
        # Redirect to a success page or login page
        return redirect('sendgig') 
        # Replace 'success' with your desired URL or view name
        
              
    return render(request, 'user/personal-signup.html')
        
        
        
        
        
        
        
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
