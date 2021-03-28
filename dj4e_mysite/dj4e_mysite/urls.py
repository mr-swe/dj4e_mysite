from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # path: home
    path('', TemplateView.as_view(template_name='home/main.html')),
    # path: autos? urls.py
    path('autos/', include('autos.urls')),
    # path: hello/ urls.py
    path('hello/', include('hello.urls')),
    # path: polls/ urls.py
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
