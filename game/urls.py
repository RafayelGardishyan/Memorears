from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('screen/view', views.index),
    path('screen/get', views.index),
    path('player/', views.index),
    path('player/1/view', views.index),
    path('player/2/view', views.index),
    path('player/1/get', views.index),
    path('player/2/get', views.index),
    path('settings/set', views.settings)
]
