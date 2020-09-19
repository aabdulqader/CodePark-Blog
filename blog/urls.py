from django.contrib import admin
from django.urls import path, include
from blog import views
admin.site.site_header = 'CodeP@rk'
admin.site.site_title = 'Welcome to the CodeP@rk'
admin.site.index_title = 'Welcome to this Portal'
urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('blogpost/<str:slug>', views.blogpost, name='blog'),
    path('allblogs/', views.allblogs, name='allblogs'),
    path('contact/', views.contact, name='contact'),
    ]
