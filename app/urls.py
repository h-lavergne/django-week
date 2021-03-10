from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('devs/', views.devs, name='devs'),
    path('dev/create', views.create_dev, name='create_dev'),
    path('jobs/', views.jobs, name='jobs'),
    path('job/create', views.create_job, name='create_job'),
    path('contact/', views.contact, name='contact'),
    path('companies/', views.companies, name='companies'),
    path('company/create', views.create_company, name='create_company'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    path('admin/', admin.site.urls),
]
