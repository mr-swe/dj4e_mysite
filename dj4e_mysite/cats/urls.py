from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "cats"
urlpatterns = [
    path('', views.CatView.as_view(), name='all_cat')
]
