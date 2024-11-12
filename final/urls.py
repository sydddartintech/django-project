"""
URL configuration for final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from .import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='newhome'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dash, name='dashboard'),
    path('administrator/',include('administrator.urls')),
    path('registration/', views.reg, name='registration'),
    path('savereg/', views.savereg, name='savereg'),
    path('saveregister/', views.saveregister, name='saveregister'),
    path('check_login/', views.check_login, name='check_login'),
    path('serviceprovider/', include('serviceprovider.urls')),
    path('client/', include('client.urls')),
    path('client_reg/', views.client_reg, name='client_reg'),
    path('save_cli/', views.save_cli, name='save_cli'),
    path('c_register/', views.c_register, name='c_register'),




    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


   

    


    


