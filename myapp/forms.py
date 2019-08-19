
from .models import TodoTask
from django import forms

#This is form to be used for Create and Update Task
class TodoTaskForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title',"maxlength":"20" ,'pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
    class Meta:
        model = TodoTask
        fields = ['name']