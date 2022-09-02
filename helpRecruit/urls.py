"""helpRecruit URL Configuration

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
from recruitment import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.job_description_view, name='jobdescription'),
    path("register/", views.register, name="register"),
    path("login/", views.login, name='login'),
    path("logout/", views.log_out, name="logout"),
    path("detail/<str:pk>",views.detail_view,name="detail"),
    path("detail/application_form/<str:pk>",views.applied_job,name='apply'),

]
