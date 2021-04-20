from django.urls import path, reverse_lazy
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.StoreListView.as_view(), name='all'),
    path('<int:pk>/detail', views.StoreDetailView.as_view(), name='store_detail'),
    path('create',
         views.StoreCreateView.as_view(success_url=reverse_lazy('store:all')), name='store_create'),
    path('<int:pk>/update',
         views.StoreUpdateView.as_view(success_url=reverse_lazy('store:all')), name='store_update'),
    path('<int:pk>/delete',
         views.StoreDeleteView.as_view(success_url=reverse_lazy('store:all')), name='store_delete'),
]