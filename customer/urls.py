from django.urls import path
from . import views

app_name = 'customer'

customer_urlpatterns = [
    path('sendgig', views.sendgig_view, name='sendgig'), 
    path('profile/', views.profile_page, name="profile"),
    path('payment_method/', views.payment_page, name="payment"),
    path('create_gig/', views.create_gig, name="create_gig"),
]