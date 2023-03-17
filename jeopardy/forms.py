from django import forms
from .models import *

class TeamForm(forms.ModelForm):
    def __init__(self,  *args,  **kwargs):
        question_id = kwargs.pop('question_id')
        super().__init__(*args, **kwargs)
        self.fields["correct"].queryset = Question.objects.filter(id=question_id)
        self.fields["incorrect"].queryset = Question.objects.filter(id=question_id)
    class Meta:
        model = Team
        fields = ["teamName", "correct", "incorrect"]