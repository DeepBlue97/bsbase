"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from django.views.static import serve as serve_static
# from backend.settings import STATICFILES_DIRS, STATIC_ROOT
# from django.views import static
from django.conf import settings
from .views import testjson

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('/', TemplateView.as_view(template_name="index.html")),
    # path('static/<path:path>', serve_static, {'document_root': STATIC_ROOT},),  # 处理静态文件
    path('api/', testjson),
    #path('', TemplateView.as_view(template_name='index.html')),
    path(r'^static/(?P<path>.*)$', serve_static, {'document_root': settings.STATIC_ROOT}, name='static'),
    
]

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     **url(r'^$', TemplateView.as_view(template_name="index.html")),**
#     url(r'^api/', include('backend.urls', namespace='api'))
# ]
