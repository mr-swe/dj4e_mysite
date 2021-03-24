from django.contrib import admin
from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # path: polls/ views/ Index
    path('', views.Index.as_view(), name='index'),
    # path: polls/ views/ Detail
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
]
