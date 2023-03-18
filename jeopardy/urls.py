'''
MIT License
Copyright (C) 2023 Leo O. Pratt-Thomas
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
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
    path("editScore/<int:team_id>", edit_team, name = "team"),
    path("question/<int:question_id>/<int:team_id>", question, name="question"),
] 
#urlpatterns.extend(TestForm.as_urls())