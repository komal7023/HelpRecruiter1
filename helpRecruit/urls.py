from django.contrib import admin
from django.urls import path
from recruitment import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.job_description_view, name='jobdescription'),
    path("register/", views.register, name="register"),
    path("login/", views.login, name='login'),
    path("logout/", views.log_out, name="logout"), 
    path("detail/<str:pk>",views.detail_view,name="detail"),
    path("detail/application_form/<str:pk>",views.application_view,name='apply'),
    path("applied-jobs/",views.applied_job,name='applied'), 
    

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
