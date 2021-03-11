from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),


    path('developer/', views.developer, name='developer'),
    # path('devs/', views.devs, name='devs'),
    # path('dev/<int:id>/', views.dev, name='dev'),
    # path('dev/create', views.create_dev, name='create_dev'),

    # path('jobs/', views.jobs, name='jobs'),
    # path('job/create', views.create_job, name='create_job'),
    # path('job/<int:id>/apply', views.apply_job, name='apply_job'),
    # path('job/<int:id>/applications', views.list_job_applications, name='list_job_applications'),
    path('job/<int:id>/', views.job_detail, name='job_detail'),
    path('job/<int:job_id>/accept/<int:dev_id>', views.accept_dev_on_job, name='accept_dev_on_job'),
    path('job/<int:job_id>/decline/<int:dev_id>', views.decline_dev_on_job, name="decline_dev_on_job"),
    path('job/create/', views.create_job, name='create_job'),
    path('job/<int:id>/edit', views.edit_job, name='edit_job'),

    # path('companies/', views.companies, name='companies'),
    # path('company/<int:id>/', views.company, name='company'),
    
    path('company/', views.company, name='company'),

    path('register/', views.register, name='register'),
    path('register/company', views.register_company, name='register_company'),
    path('register/developer', views.register_developer, name='register_developer'),
    
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()