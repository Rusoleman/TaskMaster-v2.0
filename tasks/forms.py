from django import forms
from .models import Task

 
class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget = forms.TextInput(attrs={
        "placeholder": "New Task"
        }),
        label = 'Task Name',
        label_suffix=''
    )
    description = forms.CharField(
        widget = forms.Textarea(attrs={
            "rows":3,
            "placeholder": "Make something"
        }),
        label_suffix=''
    )
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority','status']