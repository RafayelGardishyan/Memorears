from django.urls import path
from . import views

urlpatterns = [
    path('player', views.playerscreen),
    path('create', views.create),
    path('lobby', views.lobby),
    path('online', views.index),
]
