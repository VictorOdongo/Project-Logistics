from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import Personal, Entreprise, Driver


def home_view(request):
    return render(request, 'home.html')

def getstarted_view(request):
    return render(request, 'user/getstarted.html')

# Personal views
# Handle personal signup form submission
def personal_signup(request):
    if request.method == 'POST':
        u_name = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        
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
            user.mobile = mobile
            user.save()
            
        personal = Personal.objects.create(
                user=user,
                username=u_name,
                firstname=firstname,
                lastname=lastname,
                mobile=mobile,
                email=email,
                password=password
            )
        user.set_password(password)
        personal.save()
        subject = 'welcome to DriveX!'
        message = f'Hello {user.username}, thank you for signing up fo DriveX delivery service.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('/sender-login')
            
    else:     
        return render(request, 'user/personal-signup.html')
    
#Send welcome email to new user
# def send_welcome_email(user_email, user_name):
#     subject = 'Welcome to DriveX'
#     html_message = render_to_string('user/welcome_email.html', {'user_name': user_name})
#     plain_message = strip_tags(html_message)
#     from_email = settings.EMAIL_HOST_USER
#     to_email = user_email

#     send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
    
# Handle personal login form submission
# Perform authentication and login logic for personal user
def sender_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('customer:sendgig')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('user:sender-login')
    
    return render(request, 'user/sender-login.html')

# Logout user
def logout(request):
    auth_logout(request)
    return redirect('/')


 # Enterprise views
 # Handle enterprise signup form submission          
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
            return redirect('/entreprise-signup')
        elif User.objects.filter(username=bizname).exists():
            messages.info(request, 'business name taken!')
            return redirect('/entreprise-signup')
        
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
            
        personal = Entreprise.objects.create(
                user=user,
                business_name=bizname,
                firstname=firstname,
                lastname=lastname,
                mobile=mobile,
                email=email,
                password=password
            )
        user.set_password(password)
        personal.save()
        subject = 'welcome to DriveX!'
        message = f'Hello {user.username}, thank you for signing up fo DriveX delivery service.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('/sender-login')
        
    else:
         return render(request, 'user/entreprise-signup.html')


# Driver views
# Handle driver signup form submission
def driver_signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        license = request.POST['license']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'email already exists!')
            return redirect('/driver-signup')
        elif User.objects.filter(username=license).exists():
            messages.info(request, 'driver license already exists!')
            return redirect('/driver-signup')
        
        else:
            user = User.objects.create_user(
            username=license,
            email=email,
            password=password
        )
            user.first_name = firstname
            user.last_name = lastname
            user.mobile = mobile
            user.save()
            
        personal = Driver.objects.create(
                user=user,
                firstname=firstname,
                lastname=lastname,
                license=license,
                mobile=mobile,
                email=email,
                password=password
            )
        user.set_password(password)
        personal.save()
        subject = 'welcome to DriveX!'
        message = f'Hello {user.username}, thank you for signing up fo DriveX delivery service.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('/driver-login')
            
    else:
        return render(request, 'user/driver-signup.html')

# Handle driver login form submission
# Perform authentication and login logic for driver user
def drive_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/drivegig')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('user:driver-login')
    
    return render(request, 'user/driver-login.html')

# def sendgig_view(request):
#     return render(request, 'customer/sendgig.html')

def drivegig_view(request):
    return render(request, 'user/drivegig.html')

def policy(request):
    return render(request, 'user/policy.html')

def profile_page(request):
    return render(request, 'customer/profile.html')

login_required(login_url="/sender-login?next=/customer/")
def create_gig(request):
         
    return render(request, 'customer/create_gig.html')
        
        
