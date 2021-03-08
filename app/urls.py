from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devs/', views.devs, name='devs'),
    path('companies/', views.companies, name='companies'),
    path('job/<int:job_id>/', views.details, name='job_details'),
    path('admin/', admin.site.urls),
]
