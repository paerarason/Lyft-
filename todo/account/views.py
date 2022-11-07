
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from.models import Task
from django.urls import reverse
from django.views.generic.list import ListView
# Create your views here.
class TaskList(ListView):
   model=Task