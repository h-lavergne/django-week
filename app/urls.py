from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devs/', views.devs, name='devs'),
    path('jobs/', views.jobs, name='jobs'),
    path('companies/', views.companies, name='companies'),
    path('admin/', admin.site.urls),
]
