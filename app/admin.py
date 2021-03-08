from django.contrib import admin

from app.models import Job
from app.models import Developer
from app.models import Company


admin.site.register(Job)
admin.site.register(Developer)
admin.site.register(Company)