from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from tablib import Dataset
import numpy as np

# Create your views here.
def main_page(request):
    questions = Question.objects.all()
    topics = Topic.objects.all()
    points = Point.objects.all()


    questions_parced = []
    for point in points:
        points_list = []
        
        #find compatiblity with qustions
        for question in questions:
            if question.points == point:
                points_list.append(question)

        questions_parced.append(points_list)


    context = {"questions": questions_parced, "topics": topics}
    return render(request, 'jeopardy/jeopardy.html', context)
        

    
