from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('getstarted', views.getstarted_view, name='getstarted'),
    path('personal-signup', views.personal_signup, name='personal-signup'),
    path('entreprisesignup', views.entreprise_signup, name='entreprise-signup'), 
    path('driver-signup', views.driver_signup, name='driver-signup'), 
    path('driver-login', views.drive_login, name='driver-login'), 
    path('sender-login', views.sender_login, name='sender-login'),    
    path('sendgig', views.sendgig_view, name='sendgig'), 
    path('drivegig', views.drivegig_view, name='drivegig'),
    path('logout', views.logout, name='logout'), 
]