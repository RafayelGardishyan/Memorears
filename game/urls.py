from django.urls import path
from . import views

urlpatterns = [
    path('getgame', views.get),
    path('getgame/<int:id>', views.getwid),
    path('setonline/<int:id>', views.setonline),
    path('changeturn', views.change_turn),
    path('set/score/<int:player>/<int:plus>', views.setscore),
    path('set/opencard/<int:cardid>', views.setopencard),
    path('set/resetcards', views.reset),
    path('set/resetscore', views.resetscore),
    path('player', views.playerscreen),
    path('create', views.create),
    path('lobby', views.lobby),
    path('online', views.index)
]
