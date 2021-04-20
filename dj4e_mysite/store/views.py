from django.shortcuts import render
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from .models import Store


# Create your views here.
class StoreListView(OwnerListView):
    model = Store
    template_name = 'store/store_list.html'
    context_object_name = 'stores'


class StoreDetailView(OwnerDetailView):
    model = Store
    template_name = 'store/store_detail.html'


class StoreCreateView(OwnerCreateView):
    model = Store
    template_name = 'store/store_form.html'
    fields = ['name', 'type']


class StoreUpdateView(OwnerUpdateView):
    model = Store
    template_name = 'store/store_form.html'
    fields = ['name', 'type']


class StoreDeleteView(OwnerDeleteView):
    model = Store
    template_name = 'store/store_confirm_delete.html'
