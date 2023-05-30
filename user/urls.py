from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('getstarted', views.getstarted_view, name='getstarted'),
    path('personal', views.personal_view, name='personal-signup'),
    path('entreprise', views.business_view, name='entreprise-signup'), 
    path('driver', views.driver_view, name='driver-signup'), 
    path('drive', views.drive_view, name='driver-login'), 
    path('sender', views.sender_view, name='sender-login'),    
    path('sendgig', views.sendgig_view, name='sendgig'), 
    path('drivegig', views.drivegig_view, name='drivegig'),
    path('logout', views.logout, name='logout'), 
]