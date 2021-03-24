from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views import View

# Create your views here.
def index(request):
    return render(request, 'polls/index.html')

# class Index(ListView):
#     template_name = "polls/index.html"
