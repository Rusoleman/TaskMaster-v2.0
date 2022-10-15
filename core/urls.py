"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tasks.views import getTasks, createTask, deleteTask, updateTask
from reminders.views import getReminders, addReminder, updateReminder, removeReminder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',getTasks, name='tasks'),
    path('createtask/',createTask, name='create_task'),
    path('delete/<int:task_id>/',deleteTask, name='delete_task'),
    path('update/<int:task_id>/',updateTask, name='update_task'),
    path('reminders/',getReminders, name='reminders'),
    path('reminders/add/',addReminder, name='add_reminder'),
    path('reminders/update/<int:reminder_id>/',updateReminder, name='update_reminder'),
    path('reminders/remove/<int:reminder_id>/',removeReminder, name='remove_reminder'),
]
