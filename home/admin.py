from django.contrib import admin

from .models import FAQ, About, ContactMessage, Customers, Images, Product, ProductCategory, Project, ProjectCategory, Service, Slider, Team, Video

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'created']

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created']
    prepopulated_fields = {'slug': ('title',)}

class ProjectImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_category', 'status', 'slug', 'created']
    list_filter = ['project_category']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_category', 'status', 'slug', 'created']
    list_filter = ['product_category']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_detail', 'status', 'created']


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'status', 'created']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'created', 'status']
    readonly_fields = ('full_name', 'subject', 'email', 'message', 'ip')
    list_filter = ['status']


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['hero_text', 'status', 'created']
    

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_link', 'status', 'created']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'status']