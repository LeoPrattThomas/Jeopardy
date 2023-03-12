from django.contrib import admin
from django.urls import include, path
from .views import *
from django.urls import path
from . import views  
from config import settings
from django.conf.urls.static import static

urlpatterns = [
    
]


urlpatterns =[
    path("",main_page, name='home'),
] 
#urlpatterns.extend(TestForm.as_urls())