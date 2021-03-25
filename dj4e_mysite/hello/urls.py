from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "hello"
urlpatterns = [
    path('', views.ssfun, name='ssfun'),
    path('cookie/', views.cookie, name='cookie')
]
