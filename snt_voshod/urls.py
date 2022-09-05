"""snt_voshod URL Configuration

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
from django.urls import path, include
from sntVoshod import views

urlpatterns = [
    path('snt-voshodAdmin/', admin.site.urls),
    path('', include('sntVoshod.urls', namespace='sntVoshod')),
    path('forum/', include('forum.urls'))
]


# Обработчик кода 404
handler404 = 'sntVoshod.views.error_404'
