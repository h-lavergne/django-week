from django.contrib import admin

from app.models import Job, Developer, Company, Contact, UserProfile

admin.site.register(Job)
admin.site.register(Developer)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(UserProfile)