from .models import Job, Developer, Company, ContactForm, CompanyRegisterForm, DeveloperRegisterForm
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def index(request):   
    if not request.user.is_authenticated:
        return redirect('/login')
         
    if hasattr(request.user, 'dev') and request.user.dev :
        return redirect('/developer')
    
    if hasattr(request.user, 'company') and request.user.company :
        return redirect('/company')
    

def about(request):
    return render(request, 'app/about.html')


def contact(request):
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
        else: 
            for field in contact:
                if len(field.errors) > 0 :
                    messages.error(request, field.label + ': ' + field.errors[0])
                
            return render(request, 'app/contact.html', {
                'form': contact
            })
            
    c = ContactForm()
    return render(request, 'app/contact.html', {
                'form': c
            })


@login_required
def developer(request):
    if not request.user.dev :
        return HttpResponseForbidden()
    
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)
    return render(request, 'app/dev/index.html', {
        "jobs": jobs
    })


@login_required
def company(request):
    if not request.user.company:
        return HttpResponseForbidden()
    
    jobs = Job.objects.filter(company=request.user.company)
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)
    
    return render(request, 'app/company/index.html', {
        'jobs': jobs
    })


@login_required
def job_detail(request, id):
    job = Job.objects.get(pk=id)
    
    if request.method == 'POST':
        if request.user.dev:
            if request.user.dev in job.applications.all():
                return
            job.applications.add(request.user.dev)
            job.save()
            send_mail(
                'Application to job offer : ' + job.title,
                'Hello ' + job.company.name + ', we are happy to tell you that ' + request.user.dev.first_name + ' ' + request.user.dev.last_name + ' has applied to your job offer : ' + job.title + ' !',
                request.user.email,
                [job.company.user.email],
                fail_silently=False,
            )
            messages.success(request, 'You applied for this job successfully')
            return redirect('/developer')
        else:
            return HttpResponseForbidden()
        
    return render(request, 'app/job_details.html', {
        'job': job
    })


@login_required
def edit_job(request, id):
    if request.method == 'POST': 
        job = get_object_or_404(Job, pk=id)
        job.title = request.POST['title']
        job.description = request.POST['description']
        job.duration = request.POST['duration']
        job.company = request.user.company
        job.salary = request.POST['salary']
        job.save()
        messages.success(request, 'Your job offer has been modified')
        return redirect('/')
    
    return redirect('/job/' + id)
   
   
@login_required     
def create_job(request):
    if not request.user.company:
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        job = Job()
        job.title = request.POST['title']
        job.description = request.POST['description']
        job.duration = request.POST['duration']
        job.company = request.user.company
        job.salary = request.POST['salary']
        job.save()
        messages.success(request, 'Your job offer has been modified')
        return redirect('/')
    
    return render(request, 'app/company/create_job.html')


@login_required
def accept_dev_on_job(request, job_id, dev_id):
    if not request.user.company :
        return HttpResponseForbidden()
  
    job = get_object_or_404(Job, pk=job_id)
    dev = get_object_or_404(Developer, pk=dev_id)
  
    if request.method == 'POST':
        if dev in job.applications.all():
            job.accepted_dev = dev
            job.save()
            messages.success(request, 'This appliers has been accepted for your job !')
            send_mail(
                'Application to job offer : ' + job.title,
                'Hello ' + job.accepted_dev.first_name + ' ' + job.accepted_dev.last_name + ', we are happy to tell you that your application have been accepted by' + job.company.name + ' !',
                job.company.user.email,
                [job.accepted_dev.user.email],
                fail_silently=False,
            )
            return redirect("/")
  
        
@login_required
def decline_dev_on_job(request, job_id, dev_id):
    if not request.user.company :
        return HttpResponseForbidden()
  
    job = get_object_or_404(Job, pk=job_id)
    dev = get_object_or_404(Developer, pk=dev_id)
  
    if request.method == 'POST':
        if dev in job.applications.all():
            job.applications.remove(dev)
            job.save()
            send_mail(
                'Application to job offer : ' + job.title,
                'Hello ' + job.accepted_dev.first_name + ' ' + job.accepted_dev.last_name + ', we are sorry to tell you that your application have been declined by' + job.company.name + '.',
                job.company.user.email,
                [job.accepted_dev.user.email],
                fail_silently=False,
            )
            messages.success(request, 'You have decline this developer on your job offer')
            return redirect("/")

# AUTH & MIDDLEWARE

def register(request):
    if request.user.is_authenticated:
        if request.user.dev :
            return redirect('/developer')
        
        if request.user.company :
            return redirect('/company')
    
    return render(request, 'app/auth/register.html')


def register_company(request):
    if request.method == 'POST':
        form = CompanyRegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            company = Company()
            company.user = user
            company.name = request.POST['name']
            company.siren = request.POST['siren']
            company.address = request.POST['address']
            company.activity_sector = request.POST['activity_sector']
            company.employees_number = request.POST['employees_number']
            company.save()
            messages.success(request, 'Your account and company have been created')
            return redirect('/login')
        else :
            for field in form:
                if len(field.errors) > 0 :
                    messages.error(request, field.label + ': ' + field.errors[0])
    
    return render(request, 'app/auth/register_company.html')


def register_developer(request):
    if request.method == 'POST':
        form = DeveloperRegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            dev = Developer()
            dev.user = user
            dev.first_name = request.POST['first_name']
            dev.last_name = request.POST['last_name']
            dev.phone_number = request.POST['phone_number']
            dev.job_title = request.POST['job_title']
            dev.cv = request.FILES['cv']
            dev.email = user.email
            dev.save()
            messages.success(request, 'Your developer account has been created')
            return redirect('/login')
        else :
            for field in form:
                if len(field.errors) > 0 :
                    messages.error(request, field.label + ': ' + field.errors[0])
                    
    return render(request, 'app/auth/register_developer.html')


def login(request):
    if request.user.is_authenticated:
        if request.user.dev != None :
            return redirect('/developer')
        
        if request.user.company :
            return redirect('/company')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('/')
        else: 
            messages.error(request, 'Wrong credentials, connection impossible.')
            return redirect('/login')    
    
    return render(request, 'app/auth/login.html')

    
def logout(request):
    django_logout(request)
    return redirect('/login')
