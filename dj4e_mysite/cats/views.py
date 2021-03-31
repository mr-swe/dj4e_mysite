from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import Breed, Cat


# Create your views here.

# craete, update, delete for cat model
class CatView(LoginRequiredMixin, View):
    def get(self, request):
        bc = Breed.objects.all().count()
        cl = Cat.objects.all()
        ctx = {
            'breed_count': bc,
            'cat_list': cl,
        }
        return render(request, 'cats/cat_list.html', ctx)


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    template_name = 'cats/cat_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cat')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    template_name = 'cats/cat_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cat')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    template_name = 'cats/cat_confirm_delete.html'
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cat')


# create, update, delete for breed model

class BreedView(LoginRequiredMixin, ListView):
    model = Breed
    template_name = 'cats/breed_list.html'
    context_object_name = 'breed_list'

    def get_queryset(self):
        return Breed.objects.all()


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    template_name = 'cats/breed_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    template_name = 'cats/breed_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    template_name = 'cats/breed_confirm_delete.html'
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')
