escribio=True
jugadores = [
    {
        "nombre": "a",
        "pos_c": 1,
        "pos_f": 1,
    },

    {
        "nombre": "b",
        "pos_c": 7,
        "pos_f": 7,
    }
]
for fila in range (8):
    puntos=""
    for columna in range (8):
        escribio=True
        for jugador in jugadores:
            if fila == jugador["pos_f"] and columna == jugador["pos_c"]:
                puntos= puntos + jugador["nombre"] + " "
                escribio=False
            
        if escribio:
            puntos=puntos+". " 
              
    print(puntos)
