from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views import View


# Create your views here.

class Index(ListView):
    template_name = "polls/index.html"
