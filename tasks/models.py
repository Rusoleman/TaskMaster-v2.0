from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=100, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, default="Not Started")
    priority = models.CharField(max_length=30, default="Low")

    def __str__(self):
        return self.title