from django.contrib import admin
from django.urls import path
from test1.views import *

urlpatterns = [
    path('',home,name='home'),
    path('contact/',contact,name='contact'),
    path('/contacts/detail/<int:id>', detail, name="detail"),
]