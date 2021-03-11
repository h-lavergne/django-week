from django.db import models
from django import forms
from django.contrib.auth.models import User
    
class Developer(models.Model):
    user = models.OneToOneField(User, related_name='dev', on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    job_title = models.CharField(max_length=200)
    email = models.EmailField()
    cv = models.FileField(upload_to='uploads/')
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Company(models.Model):
    user = models.OneToOneField(User, related_name='company', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    siren = models.CharField(max_length=9)
    address = models.CharField(max_length=200)
    activity_sector = models.CharField(max_length=200)
    employees_number = models.IntegerField()
    def __str__(self):
        return self.name
    
class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    duration = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    applications = models.ManyToManyField(Developer, blank=True, related_name="applications")
    accepted_dev = models.ForeignKey(Developer, on_delete=models.CASCADE, null=True, blank=True)
    salary = models.IntegerField()
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length = 400)
    message = models.TextField()
    def __str__(self):
        return self.email + ' - ' + self.subject     
        

class CompanyRegisterForm(forms.ModelForm):
    class Meta :
        model = Company
        fields = ['name', 'siren', 'address', 'activity_sector', 'employees_number']  

class ContactForm(forms.ModelForm):
    class Meta :
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        
class DeveloperRegisterForm(forms.ModelForm):
    class Meta :
        model = Developer
        fields = ['first_name', 'last_name', 'job_title', 'email', 'phone_number', 'cv']
        
class JobForm(forms.ModelForm):
    class Meta :
        model = Job
        fields = '__all__'