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