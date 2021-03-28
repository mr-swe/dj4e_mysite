from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View

from .models import Make, Autos


# Create your views here.

class AutosView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.all().count()
        al = Autos.objects.all()
        ctx = {
            'make_count': mc,
            'auto_list': al,
        }
        return render(request, 'autos/auto_list.html', ctx)

