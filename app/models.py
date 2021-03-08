from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
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
