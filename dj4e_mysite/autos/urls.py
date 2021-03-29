from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "autos"
urlpatterns = [
    path('', views.AutoView.as_view(), name='all'),  # path: default page for autos apps/route
    path('lookup/', views.MakeView.as_view(), name='make_list'),  # path: for make list view
    path('main/create/', views.AutoCreate.as_view(), name='auto_create'),  # path: autos/ views/ AutoCreate
    path('main/<int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),  # path: autos/ views/ AutoUpdate
    path('main/<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete')
]
