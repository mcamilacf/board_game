from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game', views.new_game, name='new-game'),
    path('game/<int:pk>/players', views.players, name='game-players'),
    path('game/<int:pk>/play', views.play_game, name='play-game'),
    path('game/<int:pk>/winers', views.winers, name='play-winers'),
]