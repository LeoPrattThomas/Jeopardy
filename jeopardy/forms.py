'''
MIT License
Copyright (C) 2023 Leo O. Pratt-Thomas
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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