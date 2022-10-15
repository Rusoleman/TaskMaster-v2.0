from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render

from .models import Reminder
from .forms import ReminderForm


def getReminders(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminders.html', {
        'reminders': reminders
    })

def addReminder(request):
    if request.method == 'GET':
        return render(request, 'add_reminder.html', {'form':ReminderForm})
    else: 
        try:
            form = ReminderForm(request.POST)
            new_reminder = form.save(commit=False)
            new_reminder.save()
            return redirect('reminders')
        except:
            return render(request, 'add_reminder.html', {
                'form':ReminderForm,
                'error':"Error"
            })

def removeReminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, pk=reminder_id)
    reminder.delete()
    return redirect('reminders')

def updateReminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, pk=reminder_id)
    if request.method == 'GET':
        form = ReminderForm(instance = reminder)
        return render(
            request, 'reminder_detail.html', 
            {
                'reminders': reminder,
                'form': form
            }
        )
    else:
        try:
            form = ReminderForm(request.POST, instance = reminder)
            reminder_updated = form.save(commit=False)
            reminder_updated.save()
            return redirect('reminders')
        except:
            return render(
                request, 
                'reminder_detail.html',
                {
                    'reminders': reminder,
                    'form': form,
                    'error': "An error has occurred while updating your Reminder!"
                })
