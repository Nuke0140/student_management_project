"""isbm_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings # 5. import these 3 to set media file 
from django.conf.urls.static import static

# 7. we need import that all views that we create  
from .import views,Hod_views,Staff_views,Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    #login path path
    path('',views.Login,name='login'),
    path("doLogin",views.doLogin,name="doLogin"), 



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # 6. here  we set our media files 
