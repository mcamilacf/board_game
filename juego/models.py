from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=250)
    actual_turn = models.IntegerField(default=0)

    def get_actual_player (self):
        players = self.player_set.all().order_by('turn')
        if len(players) == 0:
            return None
        return players[self.actual_turn % len(players)]
    def get_next_player (self):
        players = self.player_set.all().order_by('turn')
        if len(players) == 0:
            return None
        if self.actual_turn % len(players) == len(players)-1:
            return players[0]
        else:
            return players[ self.actual_turn % len(players) + 1]
    def get_previous_player (self):
        players = self.player_set.all().order_by('turn')
        if len(players) == 0:
            return None
        if self.actual_turn % len(players) == 0:
            return players[len(players)-1]
        else:
            return players[ self.actual_turn % len(players) - 1]
    
    def end_turn (self):
        self.actual_turn += 1
        self.save()

        

class Player(models.Model):
    red = 'red'
    blue = 'blue'
    green = 'green'
    yellow = 'yellow'
    purple = 'purple'
    orange = 'orange'

    color_choices = (
        (red, 'Rojo'),
        (blue, 'Azul'),
        (green, 'Verde'),
        (yellow, 'Amarrillo'),
        (purple, 'Morado'),
        (orange, 'Naranja'),
    )

    turn_choices = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
    )
    
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    color = models.CharField(max_length=20, choices=color_choices, default=red)
    coordinate_x = models.IntegerField(default=0)
    coordinate_y = models.IntegerField(default=0)
    turn = models.IntegerField(choices=turn_choices)
    points = models.IntegerField(default=0)
    winer = models.BooleanField(default=False)
    

class Card(models.Model):
    challenge = 'challenge'
    true = 'true'
    question = 'question'
    penalty = 'penalty'

    card_choices = (
        (challenge, 'Reto'),
        (true, 'Verdad'),
        (question, 'Pregunta'),
        (penalty, 'Castigo'),
    )
    type = models.CharField(max_length=20, choices=card_choices)
    text = models.CharField(max_length=300)
    active = models.BooleanField(default=True)

    @property
    def color(self):
        colors = {
            self.challenge: 'red',
            self.true: 'green',
            self.question: 'blue',
            self.penalty: 'black',

        }
        return colors[self.type]

class Board(models.Model):
    column_number = models.IntegerField(default=8)
    row_number = models.IntegerField(default=8)
    game = models.OneToOneField(Game, on_delete=models.CASCADE)

class Box(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True)
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    
