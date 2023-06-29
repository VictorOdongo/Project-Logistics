from django.urls import path
from driver import views
from django.conf import settings
from django.conf.urls.static import static
from driver import apis as courier_apis

app_name = 'driver'

urlpatterns = [
    path('drivegig', views.drivegig_view, name='drivegig'),
    path('api/available/gigs', courier_apis.available_jobs_api, name='available_jobs_api')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)