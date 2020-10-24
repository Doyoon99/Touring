"""touring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import sociallogin.views
import tourPlan.views
import commentcrud.views
import recommend.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sociallogin.views.home, name='home'),
    path('login/', sociallogin.views.login, name='login'),
    path('info/', sociallogin.views.info, name='info'),
    path('accounts/', include('allauth.urls')),
    path('commentcrud/', include('commentcrud.urls')),
    path('Schedule/', include('Schedule.urls')),
    path('tourPlan/', include('tourPlan.urls')),
    path('recommend/', include('recommend.urls')),
]
