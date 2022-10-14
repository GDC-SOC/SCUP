from django.urls import path

from . import views

urlpatterns = [
    path('mosaic', views.mosaic, name="mosaic"),
    path('cape', views.cape, name="cape"),
    path('aether', views.aether, name="aether")
]