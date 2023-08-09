from django.contrib import admin
from django.urls import path,include
from taskapp  import views as task_view
urlpatterns=[
    path('',task_view.home,name='home'),
    path('contact/',task_view.contact,name='contact'),
    path('about/',task_view.about,name='about'),
    path('daylist/',task_view.daylist,name='daylist'),
    path('daylist/<int:day>/',task_view.handleday,name='day'),



]