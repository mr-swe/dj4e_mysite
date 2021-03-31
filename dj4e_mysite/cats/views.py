from django.shortcuts import render
from django.views import View

from .models import Breed, Cat


# Create your views here.
class CatView(View):
    def get(self, request):
        bc = Breed.objects.all().count()
        cl = Cat.objects.all()
        ctx = {
            'breed_count': bc,
            'cat_list': cl,
        }
        return render(request, 'cats/cat_list.html', ctx)
