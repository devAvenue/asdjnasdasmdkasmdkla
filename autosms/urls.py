"""autosms URL Configuration

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
from polls.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index),
    path('main/', index),
    path('free_number/', free_number),
    path('active_number/', active_number),
    path('activeite/', activeite),
    path('activeites/', activeites),
    path('FAQ/', faq),
    path('admin/', admin.site.urls),
    path('rent_active/', rent_active),
    path('rent_active/show_number/', show_number),
    path('pay/', pay),
    path('my_profile/', my_profile),
    path('change_password/', change_password),
    path('my_number/', my_number),
    path('exit/', exit),
    path('req_auth/', reg_auth),
    path('chek_number/', chek_number),
    path('free_number/chek_number/', chek_number),
    path('active_number/chek_number/', chek_number),
    path('FAQ/chek_number/', chek_number),
    path('rent_number/chek_number/', chek_number),
    path('exit/chek_number/', chek_number),
    path('main/chek_number/', chek_number),
    path('rent_active/chek_number/', chek_number),
    path('pay/chek_number/', chek_number),
    path('rent_time/', rent_time),
    path('rent_time/chek_number/', chek_number),
]
#${window.location.protocol}/chek_number?chek_number=USA&limit=Отключен
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


