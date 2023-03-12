from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import render

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

def question(request, question_id):
    question = Question.objects.get(id = question_id)
    return render(request, 'jeopardy/question.html', {"question": question})



        

    
