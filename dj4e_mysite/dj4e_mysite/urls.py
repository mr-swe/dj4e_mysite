from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html')),  # path: home
    # path('cats/', include('cats.urls')),  # path: cats/ urls.py
    # path('autos/', include('autos.urls')),  # path: autos/ urls.py
    # path('hello/', include('hello.urls')),  # path: hello/ urls.py
    # path('polls/', include('polls.urls')),  # path: polls/ urls.py
    path('accounts/', include('django.contrib.auth.urls')),  # path for django login feature
    path('admin/', admin.site.urls),
]
