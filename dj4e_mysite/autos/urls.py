from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "autos"
urlpatterns = [
    path('', views.AutosView.as_view(), name='all'),  # path: default page for autos apps/route
    path('lookup/', views.MakeView.as_view(), name='make_list'),  # path: for make list view
]
