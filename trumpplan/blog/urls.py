from django.conf.urls import url

from . import views

urlpatterns = [url(r'^flash', views.index_flash),]