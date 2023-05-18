from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('getstarted/', views.getstarted_view, name='getstarted'),
    path('getstarted/', views.getstarted_view, name='getstarted'),
    path('getstarted/', views.getstarted_view, name='getstarted'),    
]