from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Question, Choice


# Create your views here.

class Index(ListView):
    template_name = "polls/index.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class Detail(DetailView):
    template_name = 'polls/detail.html'
    model = Question
