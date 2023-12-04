
from django.contrib import admin
from django.urls import path
from purityapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('gallery/', views.gallery, name='gallery'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('products/', views.products, name='products'),
    path('appointment/', views.appointment, name='appointment'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('pay/', views.pay, name='pay'),
    path('token/', views.token, name='token'),
    path('stk/', views.stk, name='stk'),
    path('ordered/', views.ordered, name='ordered'),

    path('upload/', views.upload_image, name='upload'),
    path('image/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    ]