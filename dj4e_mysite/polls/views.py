from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class Index(View):
    

def index(request):
    return HttpResponse("Mahfuzur Rahman")