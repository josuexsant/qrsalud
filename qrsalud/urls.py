"""qrsalud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from qr_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.default, name='index'),
    path('signin/', views.signin, name='signin'),
    path('form/<str:pk>/', views.update_report, name='form'),
    path('qr/<str:pk>/', views.read_filter_report, name='qr'),
    path('saved/', views.saved, name='saved'),
    path('info/', views.info, name='info'),
    path('salir/', views.signout, name='logout'),
    path('settings/', views.settings, name='settings'),
    path('delete/<str:pk>/', views.delete_report, name='delete'),
]
