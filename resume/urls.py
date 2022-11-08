from django.urls import path
from .import views

urlpatterns=[
     
    path('',views.index,name='index'),
    path('resumepdf/<int:id>',views.Resumepdf,name="resumepdf"),
    path('login',views.loadlogin, name='login'),
    path('home',views.home, name='home'),
    path('register',views.loadregister, name='register'),
    path('reg',views.register),
    path('userlogin',views.Userlogin),
    path('logout',views.Userlogout,name='logout'),
    path('listuser',views.listuser,name='listuser'),
    path('contact',views.contact,name='contact'),
    

]