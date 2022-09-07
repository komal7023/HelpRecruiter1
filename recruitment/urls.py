from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('recruitment.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)