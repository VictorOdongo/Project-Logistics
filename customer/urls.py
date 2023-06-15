from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'customer'

urlpatterns = [
    path('sendgig', views.sendgig_view, name='sendgig'), 
    path('profile/', views.profile_page, name="profile"),
    path('payment_method/', views.payment_method, name="payment_method"),
    path('create_gig/', views.create_gig, name="create_gig"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)