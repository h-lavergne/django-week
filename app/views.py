from .models import Job, Developer, Company, ContactForm
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

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
    paginator = Paginator(devs, 2) # Show 10 devs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/devs/index.html', {
        "page_obj": page_obj
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

def contact(request):
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
        else: 
            return render(request, 'app/contact.html', {
                'form': contact
            })
            
    c = ContactForm()
    return render(request, 'app/contact.html', {
                'form': c
            })