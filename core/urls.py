from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.admin import OTPAdminSite
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap
}

class OTPAdmin(OTPAdminSite):
    pass

admin_site = OTPAdmin(name="OTPAdmin")

admin_site.register(User)
admin_site.register(TOTPDevice)

from home import views

handler400 = 'core.views.handler400'
handler403 = 'core.views.handler403'
handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500'
handler503 = 'core.views.handler503'

urlpatterns = [
    path('django_admin/', admin.site.urls),
    path('admin/', admin_site.urls),
    
    path('', include('home.urls', namespace='home')),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('products', views.all_products, name='all_products'),
    path('projects', views.all_projects, name='all_projects'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('clients', views.clients, name='clients'),

    path('services/<slug:slug>', views.service_detail, name='service_detail'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('<slug:product_category_slug>/', views.prod_cat_list, name='prod_cat_list'),
    path('project-category/<slug:project_category_slug>/', views.proj_cat_list, name='proj_cat_list'),


    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^robots.txt', include('robots.urls')),
    re_path(r'^maintenance-mode/', include('maintenance_mode.urls')), # This is to enable us to toggle on/off via super_user url
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)