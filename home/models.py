from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.forms import ModelForm, TextInput, Textarea

class Service(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    short_detail = models.CharField(max_length=500)
    detail = RichTextUploadingField(blank=True)
    short_image = models.ImageField(upload_to='images/')
    short_alt = models.CharField(max_length=160)    
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=160)
    slug = models.SlugField(max_length=255, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Services'
    
    def get_absolute_url(self):
        return reverse('service_detail', args=[self.slug])
    
    def __str__(self):
        return self.title


class Team(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=160)
    facebook = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    linkedin = models.CharField(max_length=150)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProjectCategory(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=250)
    detail = RichTextUploadingField(blank=True)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=160)
    slug = models.CharField(max_length=250, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Project Categories'
    
    def get_absolute_url(self):
        return reverse('proj_cat_list', args=[self.slug])

    def __str__(self):
        return self.title


class Project(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    project_category = models.ForeignKey(ProjectCategory, related_name='project', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    detail = RichTextUploadingField(blank=True)
    short_image = models.ImageField(upload_to='images/')
    short_alt = models.CharField(max_length=160)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=160)
    client = models.CharField(max_length=150)
    demands = models.CharField(max_length=250)
    video_link = models.CharField(max_length=30)
    video_image = models.ImageField(upload_to='images/')
    video_alt = models.CharField(max_length=160)
    similar_image = models.ImageField(upload_to='images/')
    conclusion = RichTextUploadingField(blank=True)
    results = RichTextUploadingField(blank=True)
    slug = models.CharField(max_length=250, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Projects'
        ordering = ('-created',)
    
    def get_absolute_url(self):
        return reverse('project_detail', args=[self.slug])
    
    def __str__(self):
        return self.title
    
class Images(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    alt = models.CharField(max_length=160)

    class Meta:
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=250)
    detail = RichTextUploadingField(blank=True)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=160)
    slug = models.CharField(max_length=250, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Product Categories'
    
    def get_absolute_url(self):
        return reverse('prod_cat_list', args=[self.slug])

    def __str__(self):
        return self.title

class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    product_category = models.ForeignKey(ProductCategory, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    detail = RichTextUploadingField(blank=True)
    product_size = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=160)
    similar_image = models.ImageField(upload_to='images/')
    slug = models.CharField(max_length=250, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])
    
    def __str__(self):
        return self.title

class About(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    short_detail = models.CharField(max_length=500)
    short_image = models.ImageField(upload_to='images/')
    short_alt = models.CharField(max_length=160)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=160)
    detail = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title


class Customers(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=160)
    link = models.CharField(max_length=250)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Customers'
    
    def __str__(self):
        return self.name

class Slider(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    image = models.ImageField(upload_to='images/')
    hero_text = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hero_text

class Video(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=160)
    video_link = models.CharField(max_length=250)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Videos'
    
    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    full_name = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=50)
    phone = models.CharField(blank=True, max_length=20)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'full_name': TextInput(attrs={'class': 'input', 'placeholder': 'First Name & Surname'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Phone Number'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your Message', 'rows': '5'}),
        }


class FAQ(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    question_number = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'FAQs'
    
    def __str__(self):
        return self.question