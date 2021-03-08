from django.contrib import admin

from app.models import Job
from app.models import Developer

admin.site.register(Job)
admin.site.register(Developer)