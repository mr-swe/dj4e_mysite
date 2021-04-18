from django.shortcuts import render
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from .models import Ad


# Create your views here.
class AdListView(OwnerListView):
    model = Ad
    template_name = 'ads/article_list.html'


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = 'ads/article_detail.html'


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'text']
    template_name = 'ads/article_form.html'


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text']
    template_name = 'ads/article_form.html'


class AdDeleteView(OwnerDeleteView):
    model = Ad
    template_name = 'ads/article_confirm_delete.html'
