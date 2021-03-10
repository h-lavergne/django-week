from django.db import models
from django import forms
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    company = models.CharField(max_length=50)
    def __str__(self):
        return self.title + ' - ' + self.company
    
class Developer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Company(models.Model):
    denomination = models.CharField(max_length=100)
    siren = models.CharField(max_length=9)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.denomination
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length = 400)
    message = models.TextField()
    def __str__(self):
        return self.email + ' - ' + self.subject     
        
class ContactForm(forms.ModelForm):
    class Meta :
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        
class RegisterForm(forms.ModelForm):
    role = models.CharField(max_length=100)
    class Meta :
        model = User
        fields = '__all__'
   
class CompanyForm(forms.ModelForm):
    class Meta :
        model = Company
        fields = '__all__' 
        
class DeveloperForm(forms.ModelForm):
    class Meta :
        model = Developer
        fields = '__all__'
        
class JobForm(forms.ModelForm):
    class Meta :
        model = Job
        fields = '__all__'