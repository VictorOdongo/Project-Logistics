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
    
    path('jobs/current/', views.current_jobs, name="current_jobs"),
    path('jobs/archived/', views.archived_jobs, name="archived_jobs"),
    path('jobs/<job_id>/', views.job_page, name="job"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)