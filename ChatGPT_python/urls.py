"""
URL configuration for ChatGPT_python project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from chatgpt import views
from django.views.generic import RedirectView

from django.views import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('api/', include('api.urls')),
   
    re_path(r'^fonts/(?P<rest>.*)$',   #重新定向url
            RedirectView.as_view(url='/static/fonts/%(rest)s', permanent=True)),

    re_path(r'^static/(?P<path>.*)$', static.serve,
      {'document_root': settings.STATIC_ROOT}, name='static'),
]
