from .models import Job, Developer, Company
from django.shortcuts import get_object_or_404, render


def index(request):
    jobs = Job.objects.all()
    return render(request, 'app/index.html', {
        "jobs": jobs
    })

def details(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'app/jobs/details.html', {
        'job': job
    })
    
def devs(request):
    devs = Developer.objects.all()
    return render(request, 'app/devs.html', {
        "devs": devs
    })

def companies(request):
    companies = Company.objects.all()
    return render(request, 'app/companies.html', {
        "companies": companies
    })