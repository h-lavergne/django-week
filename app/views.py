from .models import Job, Developer, Company, ContactForm, RegisterForm, CompanyForm, DeveloperForm, JobForm, UserProfile
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse



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
    paginator = Paginator(devs, 10) # Show 10 devs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/devs/index.html', {
        "page_obj": page_obj
    })

def jobs(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 10) # Show 10 devs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/jobs/index.html', {
        "page_obj": page_obj
    })
    
def companies(request):
    companies = Company.objects.all()
    paginator = Paginator(companies, 10) # Show 10 devs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/companies/index.html', {
        "page_obj": page_obj
    })
    
def create_company(request):
    auth_middleware(request)
    form = CompanyForm()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The company has been successfully created')
            return redirect('/companies')

        else:
            for field in form:
                if len(field.errors) > 0 :
                    messages.error(request, field.label + ': ' + field.errors[0])
            return redirect('/company/create')
    
    return render(request, 'app/companies/create.html')
    
def create_dev(request):
    auth_middleware(request)
    
    form = DeveloperForm()
    if request.method == 'POST':
        form = DeveloperForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The developer has been successfully created')
            return redirect('/devs')
            
        else:
            for field in form:
                if len(field.errors) > 0 :
                    messages.error(request, field.label + ': ' + field.errors[0])
            return redirect('/dev/create')
    
    return render(request, 'app/devs/create.html')

def create_job(request):
    auth_middleware(request)
    
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The job has been successfully created')
            return redirect('/jobs')
            
        else:
            for field in form:
                if len(field.errors) > 0 :
                    messages.error(request, field.label + ': ' + field.errors[0])
            return redirect('/job/create')
    
    return render(request, 'app/jobs/create.html')
   
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

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        username = request.POST['username']
        password = request.POST['password']
        userProfile = UserProfile()
        userProfile.user = user
        userProfile.role = request.POST['role']
        userProfile.save()

        user = authenticate(request, username=username, password=password)  
        
        if user is not None:
            django_login(request, user)
        else:
            messages.error(request, 'Impossible to create an account, please verify your credentials')
            return redirect('/login')
        
        return redirect('/')
        
    return render(request, 'app/auth/register.html', {
        'form': form
    })

def login(request):
    form = RegisterForm()
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
    
    return render(request, 'app/auth/login.html', {
        'form': form
    })

    
def logout(request):
    django_logout(request)
    return redirect('/login')

def auth_middleware(request):
    if request.user.is_authenticated == None :
        messages.error(request, "You need to be logged in first !")
        return redirect('/login')
    elif not request.user.is_superuser :
        messages.error(request, "You don't have access to this page !")
        return redirect('/')