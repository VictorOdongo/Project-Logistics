from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'driver'

urlpatterns = [
    path('drivegig', views.drivegig_view, name='drivegig')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)