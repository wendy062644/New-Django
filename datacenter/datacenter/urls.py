"""datacenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from mysite import views
from django.contrib import admin
from django.urls import path, include
from mysite.views import  HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home),
    path('about', views.about),
    path('spidercovid-19', views.spidercovid),
    path('spiderwater', views.spiderwater),
    path('test', views.test),
    path('test123', views.test123),
    path('profile', views.profile),
    path('work', views.work),
    path('share', views.share),
]
