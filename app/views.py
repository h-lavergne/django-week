from .models import Job, Developer, Company
from django.shortcuts import get_object_or_404, render


def index(request):
    jobs = Job.objects.all()
    devs = Developer.objects.all()
    companies = Company.objects.all()
    return render(request, 'app/index.html', {
        "jobs": jobs,
        "devs": devs,
        "companies": companies
    })
    
def devs(request):
    devs = Developer.objects.all()
    return render(request, 'app/devs/index.html', {
        "devs": devs
    })

def jobs(request):
    jobs = Job.objects.all()
    return render(request, 'app/jobs/index.html', {
        "jobs": jobs
    })
    
def companies(request):
    companies = Company.objects.all()
    return render(request, 'app/companies/index.html', {
        "companies": companies
    })
    
def about(request):
    return render(request, 'app/about.html')