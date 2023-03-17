from .models import *
from .forms import *
import random
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404

    

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
    context ={}

    context["url"] = (question_id,team_id)

    team = Team.objects.get(id = team_id)
    context["team"] = team

    question = Question.objects.get(id = question_id)
    context["question"] = question

    #edit user form
    team_obj = get_object_or_404(Team, id = team_id) # fetch the object related to passed id
    
    teamForm = TeamForm(request.POST or None, instance = team_obj, question_id = question_id)  # pass the object as instance in form
    if teamForm.is_valid():# save the data from the form
        if teamForm.has_changed():
            print("The following fields changed: %s" % ", ".join(teamForm.changed_data))

        teamForm.save()

        #chanage active tean
        team_id = team.id
        team_id += 1

        while True:
            try:
                team = Team.objects.get(id = team_id) 
                break
            except ObjectDoesNotExist:   
                team_id =+ 1
                if team_id > 99:
                    team_id = 0
                print(team_id)
                
            
    
        print(Team.objects.get(id = team_id))
        return redirect(f"/board/{ team_id }")
    context["teamForm"] = teamForm # add form dictionary to context

    return render(request, 'jeopardy/question.html', context)



        

    
