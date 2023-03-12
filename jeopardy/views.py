from .models import *
import random
from django.http import HttpResponse
from django.shortcuts import render, redirect

    

# Create your views here.
def main_page(request):
    teams = Team.objects.all()
    team = random.choice(teams)
    return redirect(f"/board/{ team.id }")


def board(request,team_id):
    questions = Question.objects.all()
    topics = Topic.objects.all()
    points = Point.objects.all()
    activeTeam = Team.objects.get(id = team_id)
    teams = Team.objects.all()

    #make ustion into a 2d array of points vs topics
    questions_parced = []
    for point in points:
        points_list = []
        #find compatiblity with qustions
        for question in questions:
            if question.points == point:
                
                points_list.append(question)
        questions_parced.append(points_list)
    
    teams_with_total = []
    for team in teams:
        score = 0
        for qusiton in team.correct.all():
            print()
            score += int(qusiton.points.points)
        teams_with_total.append((team,score))

    #local vars for HTML
    context = {
        "questions": questions_parced, 
        "topics" : topics, 
        "activeTeam" : activeTeam, 
        "team_id" : team_id,
        "teams" : teams_with_total,
        }

    return render(request, 'jeopardy/jeopardy.html', context)

def question(request, question_id, team_id):
    question = Question.objects.get(id = question_id)
    return render(request, 'jeopardy/question.html', {"question": question})



        

    
