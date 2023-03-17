'''
Copyright (C) 2023 Leo Pratt-Thomas
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
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
        team_id = next_team(team.id)
        
        print(Team.objects.get(id = team_id))
        return redirect(f"/board/{ team_id }")
    context["teamForm"] = teamForm # add form dictionary to context

    return render(request, 'jeopardy/question.html', context)

def next_team(team_id):
    team_id += 1
    while True:
        try:
            team = Team.objects.get(id = team_id) 
            break
        except ObjectDoesNotExist:   
            team_id =+ 1
            if team_id > 99:
                team_id = 0
    return team_id
        

def edit_team(request,team_id):
    team_obj = get_object_or_404(Team, id = team_id)
    teamForm = TeamForm2(request.POST or None, instance = team_obj)
    if teamForm.is_valid():
        teamForm.save()
        return redirect(f"/board/{ team_id }")
    return render(request, 'jeopardy/editTeam.html', {"teamForm":teamForm, "team_id":team_id})
        

    
