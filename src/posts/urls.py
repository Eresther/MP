from django.conf.urls import include, url
from django.contrib import admin

from .import views

app_name = 'posts'

urlpatterns = [
	url(r'^$', views.post_home, name= 'main'),
	url(r'^home/', views.post_home, name= 'home'),
    url(r'^contacts/', views.post_contact, name= 'contact'),
    url(r'^case/', views.post_case, name= 'case'),
    url(r'^ddr3/', views.post_ddr3, name= 'ddr3'),
    url(r'^ddr4/', views.post_ddr4, name= 'ddr4'),
    url(r'^gpu/', views.post_gpu, name= 'gpu'),
    url(r'^moth1150/', views.post_moth1150, name= 'moth1150'),
    url(r'^moth1151/', views.post_moth1151, name= 'moth1151'),
    url(r'^proc1150/', views.post_proc1150, name= 'proc1150'),
    url(r'^proc1151/', views.post_proc1151, name= 'proc1151'),
    url(r'^psu/', views.post_psu, name= 'psu'),
    url(r'^ssd/', views.post_store, name= 'store'),
]
