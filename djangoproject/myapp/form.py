from django import forms
from .models import Task

class MyForm(forms.ModelForm):
   class Meta:
       model = Task
       fields = ["title", "description"]
       labels = {"title" : "Title", "description" : "Description", }
