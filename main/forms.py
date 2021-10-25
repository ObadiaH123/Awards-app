from django import forms
from django.db.models import fields
from .models import *
# adding a new project

class UploadProjectForm(forms.ModelForm):
    class Meta:
        model=Award
        fields=('Name','Description','developer','created_date','image','linktosite')

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=("comment","rating")        