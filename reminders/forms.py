from django import forms
from .models import Reminder


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = [
            'title', 
            'deadline_date',
            'deadline_time',
            'state',
            'finished_on_date',
            'finished_on_time',
            'task'
        ]