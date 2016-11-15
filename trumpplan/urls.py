"""trumpplan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from .blog import views


urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^maga/$', views.index_flash, name='indexflash'),
    url(r'^test', views.index),
    url(r'^sections/(?P<key>[a-zA-Z ].+)/(?P<val>[a-zA-Z ].+)/$',
        views.load_article,
        name='section_loader'),
    url(r'^sections/(?P<key>[a-zA-Z ].+/$)',
        views.load_section,
        name='index_flash'),
    #url(r'^sections/(?P<key>[\w.@+-]+)/(?P<value>[\w.@+-]+)', views.load_article, ),

    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'))
]
