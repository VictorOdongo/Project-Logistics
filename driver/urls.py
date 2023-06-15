from django.urls import path
from . import views

app_name = 'driver'

urlpatterns = [
    path('drivegig', views.drivegig_view, name='drivegig')
]