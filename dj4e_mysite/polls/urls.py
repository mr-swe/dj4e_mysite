from django.contrib import admin
from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # path: polls/ views/ Index(class)
    path('', views.Index.as_view(), name='index'),
    # path: polls/ views/ Detail(class)
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
    # path: polls/ views/ Result(class)
    path('<int:pk>result/', views.Result.as_view(), name='result'),
    # path: polls/ views/ vote(function)
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
