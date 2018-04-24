from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('themes', views.themes_index),
    path('images', views.images_index),
    path('themes/add', views.themes_add),
    path('images/add', views.images_add),
    path('themes/delete/<int:id>', views.themes_delete),
    path('images/delete/<int:id>', views.images_delete),
]
