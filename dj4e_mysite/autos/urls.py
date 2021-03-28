from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "autos"
urlpatterns = [
    path('', views.AutosView.as_view(), name='all')
]
