from email.mime import image
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from . models import FAQ, About, ContactForm, ContactMessage, Customers, Images, Product, ProductCategory, Project, ProjectCategory, Service, Slider, Video

def home(request):
    product_category = ProductCategory.objects.all()
    projects = Project.objects.order_by('-created')[:6]
    slider = Slider.objects.all()
    service = Service.objects.order_by('-created')[:3]
    about = About.objects.all()
    video = Video.objects.all()
    customer = Customers.objects.all()
    faq = FAQ.objects.order_by('created')[:6]
    return render(request, 'index.html', {'product_category': product_category, 'projects': projects, 'slider': slider, 'service': service, 'about': about, 'video': video, 'customer': customer, 'faq': faq})


def prod_categories(request):
    return {
        'prod_categories': ProductCategory.objects.all()
    }

def prod_cat_list(request, product_category_slug):
    product_category = get_object_or_404(ProductCategory, slug=product_category_slug)
    products = Product.objects.filter(product_category=product_category)
    about = About.objects.all()
    return render(request, 'product_category.html', {'product_category': product_category, 'products': products, 'about': about})


def all_products(request):
    products = Product.objects.all()
    about = About.objects.all()
    return render(request, 'products.html', {'products': products, 'about': about})


def product_detail(request, slug):
    products = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(product_category=products.product_category).exclude(slug = slug)[:3]
    about = About.objects.all()
    return render(request, 'product_detail.html', {'products': products, 'related_products': related_products, 'about': about})


def proj_categories(request):
    return {
        'proj_categories': ProjectCategory.objects.all()
    }

def proj_cat_list(request, project_category_slug):
    project_category = get_object_or_404(ProjectCategory, slug=project_category_slug)
    projects = Project.objects.filter(project_category=project_category)
    about = About.objects.all()
    return render(request, 'project_category.html', {'project_category': project_category, 'projects': projects, 'about': about})


def all_projects(request):
    projects = Project.objects.all()
    about = About.objects.all()
    return render(request, 'projects.html', {'projects': projects, 'about': about})

def project_detail(request, slug):
    projects = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.filter(project_category=projects.project_category).exclude(slug = slug)[:3]
    about = About.objects.all()
    images = Images.objects.filter(project=projects)
    return render(request, 'project_detail.html', {'projects': projects, 'related_projects': related_projects, 'about': about, 'images': images})

def service(request):
    services = Service.objects.all()
    about = About.objects.all()
    return render(request, 'service.html', {'services': services, 'about': about})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    about = About.objects.all()
    return render(request, 'service_detail.html', {'service': service, 'about': about})

def about(request):
    about = About.objects.all()
    customer = Customers.objects.all()
    return render(request, 'about.html', {'about': about, 'customer': customer})

def contact(request):
    if request.method == 'POST':  # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()  # create relation with model
            data.full_name = form.cleaned_data['full_name']  # get form input data
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(
                request, "Your message has been sent. Thank you for your message! We'll reach out as soon as possible.")
            return HttpResponseRedirect('/contact')
    form = ContactForm
    about = About.objects.all()
    return render(request, 'contact.html', {'form': form, 'about': about})


def faq(request):
    if request.method == 'POST':  # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()  # create relation with model
            data.full_name = form.cleaned_data['full_name']  # get form input data
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(
                request, "Your message has been sent. Thank you for your message! We'll reach out as soon as possible.")
            return HttpResponseRedirect('/contact')
    faq = FAQ.objects.all()
    form = ContactForm
    about = About.objects.all()
    return render(request, 'faq.html', {'faq': faq, 'form': form, 'about': about})

def clients(request):
    customer = Customers.objects.all()
    about = About.objects.all()
    return render(request, 'clients.html', {'customer': customer, 'about': about})