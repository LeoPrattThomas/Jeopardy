from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class meta:
        model = Team
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',]