"""palomitas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from loja.views import view_peca, CreateRoupas, ViewLoja, CreateImage, view_carrinho

urlpatterns = [

    url(r'^home/$', ViewLoja.as_view(), name='home'),
	url(r'^peca/(?P<pk>[-\w]+)/$', view_peca, name='view-peca'),
    url(r'^roupas/adicionar/$', CreateRoupas.as_view(), name='add-pecas'),
    url(r'^roupas/imagem/$', CreateImage.as_view(), name='add-imagem'),
    url(r'^carrinho/$', view_carrinho, name='view-carrinho'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
