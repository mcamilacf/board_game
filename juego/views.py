from django.shortcuts import render
from .forms import GameForm
from django.shortcuts import redirect
from .models import Player, Game, Board, Box, Card
import random
from random import choices


def index(request):
    return render(request, 'juego/index.html', {})

def new_game(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            board = Board(game=game)
            board.save()
            cards = Card.objects.filter(active=True)
            box_number = board.column_number * board.row_number
            for i, card in enumerate(choices(cards, k=box_number)):
                x = i % board.column_number
                y = i // board.row_number
                print(x, y)
                box = Box(board=board, card=card, position_x=x, position_y=y)
                box.save()
            return redirect('game-players', pk=game.pk) #es el nombre de la url
    else:
        form = GameForm()
    return render(request, 'juego/new_game.html', {'form': form})

def players(request, pk):
    players = Player.objects.filter(game=pk)
    return render(request, 'juego/players.html', {'players':players,'game_pk':pk})

def play_game(request, pk):
    players = Player.objects.filter(game=pk)    
    number_of_rows_and_columns=list(range (8))
    num_die = random.randint(1, 6)
    game = Game.objects.get(pk=pk)
    board = Board.objects.get(game=pk)
    boxes = Box.objects.filter(board=board)
    actual_player = game.get_actual_player()
    next_player = game.get_next_player()
    game.end_turn()
    y = actual_player.coordinate_y
    x = actual_player.coordinate_x
    if y % 2 != 0:
        n = x - num_die
        if n < 0:
            x = n * -1 -1
            y += 1
    
        else:
            x = n
    else:
        n = x + num_die
        if n > 7:
            z = n-8
            y += 1
            x = 7-z
        else:
            x = n
    if x == 0 and y == 7:
        pass
    elif y > 7:
        x = actual_player.coordinate_x
        y = actual_player.coordinate_y
    
    actual_player.coordinate_x = x
    actual_player.coordinate_y = y
    actual_player.save()     

    return render(request, 'juego/table.html', {'num':number_of_rows_and_columns, 'players':players, 'num_die':num_die, 'game_pk':pk, 'actual_player':actual_player, 'next_player':next_player, 'boxes':boxes})

def see_game (request, pk):
    players = Player.objects.filter(game=pk)    
    number_of_rows_and_columns=list(range (8))
    num_die = ""
    game = Game.objects.get(pk=pk)
    board = Board.objects.get(game=pk)
    boxes = Box.objects.filter(board=board)
    actual_player = game.get_actual_player()
    next_player = game.get_next_player()
    previous_player = game.get_previous_player()
    if previous_player.coordinate_x == 0 and  previous_player.coordinate_y == 7:
        for player in players:
            y = player.coordinate_y
            x = player.coordinate_x
            if y % 2 != 0:
                y = y*8
                x = 7-x
                player.points = x+y+1
            else:
                y = y*8             
                player.points = x+y+1
            player.save()
        players = Player.objects.filter(game=pk).order_by('-points')
        player = players[0]
        player.winer=True
        player.save()
        return render(request, 'juego/winers.html', {'players':players,'game_pk':pk})
    else:
        return render(request, 'juego/table.html', {'num':number_of_rows_and_columns, 'players':players, 'num_die':num_die, 'game_pk':pk, 'actual_player':actual_player, 'next_player':next_player, 'boxes':boxes})


def restar_player (request, pk):
    players = Player.objects.filter(game=pk)    
    number_of_rows_and_columns=list(range (8))
    num_die = ""
    game = Game.objects.get(pk=pk)
    board = Board.objects.get(game=pk)
    boxes = Box.objects.filter(board=board)
    actual_player = game.get_actual_player()
    next_player = game.get_next_player()
    previous_player = game.get_previous_player()
    previous_player.coordinate_x = 0
    previous_player.coordinate_y = 0
    previous_player.save()
    return render(request, 'juego/table.html', {'num':number_of_rows_and_columns, 'players':players, 'num_die':num_die, 'game_pk':pk, 'actual_player':actual_player, 'next_player':next_player, 'boxes':boxes})


def card(request, pk):
    game = Game.objects.get(pk=pk)
    previous_player = game.get_previous_player()
    y = previous_player.coordinate_y
    x = previous_player.coordinate_x
    board = Board.objects.get(game=pk)
    box = Box.objects.filter(board=board).get(position_x=x, position_y=y)
    return render(request, 'juego/card.html', {'box':box, 'game_pk':pk})



def winers(request, pk):
    players = Player.objects.filter(game=pk)
    for player in players:
        y = player.coordinate_y
        x = player.coordinate_x
        if y % 2 != 0:
            y = y*8
            x = 7-x
            player.points = x+y+1
        else:
            y = y*8             
            player.points = x+y+1
        player.save()
    players = Player.objects.filter(game=pk).order_by('-points')
    player = players[0]
    player.winer=True
    player.save()
    return render(request, 'juego/winers.html', {'players':players,'game_pk':pk})
    
