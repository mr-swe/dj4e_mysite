from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "cats"
urlpatterns = [
    path('', views.CatView.as_view(), name='all_cat'),
    path('cats/create/', views.CatCreate.as_view(), name='cat_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
]
