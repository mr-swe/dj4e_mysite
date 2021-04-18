from django.shortcuts import render
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from .models import Ad


# Create your views here.
class AdListView(OwnerListView):
    model = Ad
    template_name = 'ads/ad_list.html'


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'text', 'price']
    template_name = 'ads/ad_form.html'


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text', 'price']
    template_name = 'ads/ad_form.html'


class AdDeleteView(OwnerDeleteView):
    model = Ad
    template_name = 'ads/ad_confirm_delete.html'
