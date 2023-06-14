"""
URL configuration for drive_express project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user import views

from user.customer import views as customer_views
from user.driver import views as driver_views

customer_urlpatterns = [
    # path('', customer_views.sendgig_view, name='sendgig'), 
    path('', customer_views.home, name='home'),
    path('profile/', customer_views.profile_page, name="profile"),
    path('payment_method/', customer_views.payment_page, name="payment"),
    # path('create_gig', customer_views.create_gig, name="create_gig"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('user/', include('django.contrib.auth.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
