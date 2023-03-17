'''
Copyright (C) 2023 Leo Pratt-Thomas
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
from django import forms
from .models import *
from itertools import chain
from django.forms.widgets import CheckboxSelectMultiple

class TeamForm(forms.ModelForm):
    correct = forms.ModelMultipleChoiceField(
            queryset = Question.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False)
    incorrect = forms.ModelMultipleChoiceField(
            queryset = Question.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False)
    
    def __init__(self,  *args,  **kwargs):
        question_id = kwargs.pop('question_id')
        team = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        self.fields["correct"].queryset = Question.objects.filter(correct__id = team.id)|Question.objects.filter(id = question_id)
        self.fields["incorrect"].queryset = Question.objects.filter(incorrect__id = team.id)|Question.objects.filter(id = question_id)

    class Meta:
        model = Team
        fields = ["correct", "incorrect"]

class TeamForm2(forms.ModelForm):
    class Meta:
        model = Team
        fields = ["teamName","correct", "incorrect","color"]