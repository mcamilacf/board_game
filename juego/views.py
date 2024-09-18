from django.shortcuts import render
from .forms import GameForm
from django.shortcuts import redirect
from .models import Player, Game
import random


def index(request):
    return render(request, 'juego/index.html', {})

def new_game(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            return redirect('game-players', pk=game.pk) #es el nombre de la url
    else:
        form = GameForm()
    return render(request, 'juego/new_game.html', {'form': form})

def players(request, pk):
    players = Player.objects.filter(game=pk)
    return render(request, 'juego/players.html', {'players':players,'game_pk':pk})

def play_game(request, pk):
    players = Player.objects.filter(game=pk)    
    number_of_rows_and_columns=[1,2,3,4,5,6,7,8]
    num_die = random.randint(1, 6)
    game = Game.objects.get(pk=pk)
    actual_player = game.get_actual_player()
    game.end_turn()
    y = actual_player.coordinate_y
    x = actual_player.coordinate_x
    if y % 2 == 0:
        n = x - num_die
        if n < 1:
            z = n * -1
            y += 1
            x = z+1           
        else:
            x = n
    else:
        n = x + num_die
        if n > 8:
            z = n-9
            y += 1
            x = 8-z
        else:
            x = n
    if x == 1 and y == 8:
        pass
    elif y > 8:
        x = actual_player.coordinate_x
        y = actual_player.coordinate_y
    
    actual_player.coordinate_x = x
    actual_player.coordinate_y = y
    actual_player.save()     

    return render(request, 'juego/table.html', {'num':number_of_rows_and_columns, 'players':players, 'num_die':num_die, 'game_pk':pk, 'actual_player':actual_player, })

def winers(request, pk):
    players = Player.objects.filter(game=pk)
    for player in players:
        y = player.coordinate_y
        x = player.coordinate_x
        if y % 2 == 0:
            y-=1
            y = y*8
            x-=1
            x = 8-x          
            player.points = x+y
        else:
            y-=1
            y = y*8             
            player.points = x+y
        player.save()
    players = Player.objects.filter(game=pk).order_by('-points')
    player = players[0]
    player.winer=True
    player.save()
    return render(request, 'juego/winers.html', {'players':players,'game_pk':pk})
    
