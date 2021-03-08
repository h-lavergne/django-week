from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devs/', views.devs, name='devs'),
    path('jobs/', views.jobs, name='jobs'),
    path('job/<int:job_id>/', views.details, name='job_details'),
    path('admin/', admin.site.urls),
]
