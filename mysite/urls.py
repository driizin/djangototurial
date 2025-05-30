from django.contrib import admin 
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('pessoa/', include('pessoa.urls')),  # delega para urls.py do app pessoa
    path('conta/', include('django.contrib.auth.urls')),  # login/logout padrão

path('', RedirectView.as_view(url='/conta/login', permanent=False)),

]