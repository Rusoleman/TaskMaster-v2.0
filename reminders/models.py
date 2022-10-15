from django.db import models
from tasks.models import Task


class Reminder(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    deadline_date = models.DateField()
    deadline_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    finished_on_date = models.DateField(blank=True, null=True)
    finished_on_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    state = models.BooleanField(default=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title