from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('getstarted/', views.getstarted_view, name='getstarted'),
    path('personal/', views.personal_view, name='personal-signup'),
    path('business/', views.business_view, name='business-signup'), 
    path('driver/', views.driver_view, name='driver-signup'), 
    path('drive/', views.drive_view, name='driver-login'), 
    path('send/', views.send_view, name='sender-login'),    
    path('sendgig/', views.sendgig_view, name='send'), 
    path('drivegig/', views.drivegig_view, name='drive'), 
]