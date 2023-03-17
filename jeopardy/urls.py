from django.contrib import admin
from django.urls import include, path
from .views import *
from django.urls import path
from config import settings
from django.conf.urls.static import static

urlpatterns = [
    
]


urlpatterns =[
    path("",main_page, name='main'),
    path("board/<int:team_id>", board, name= "board"),
    #path("edit_Score/<int:team_id>")
    path("question/<int:question_id>/<int:team_id>", question, name="question"),
] 
#urlpatterns.extend(TestForm.as_urls())