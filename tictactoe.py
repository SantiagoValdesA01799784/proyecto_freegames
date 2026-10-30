"""Gato (Tic Tac Toe)

Juego modificado por Santiago Valdés Cruz (A01799784).

Ejercicios

1. Darle a la X y a la O un color y grosor diferente.
2. ¿Qué pasa cuando alguien toca una casilla ocupada?
3. ¿Cómo detectarías cuando alguien ganó?
4. ¿Cómo podrías crear un jugador controlado por la computadora?
"""

from turtle import *

from freegames import line


def grid():
    """Dibuja las líneas del tablero del gato."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja la X del jugador 1."""
    # Modificación 1: X roja, más gruesa, más pequeña y centrada en la casilla
    color('red')
    width(10)
    line(x + 30, y + 30, x + 103, y + 103)
    line(x + 30, y + 103, x + 103, y + 30)


def drawo(x, y):
    """Dibuja la O del jugador 2."""
    # Modificación 1: O azul, más gruesa, de radio 40 y centrada en la casilla
    color('blue')
    width(10)
    up()
    goto(x + 66.5, y + 26.5)
    down()
    circle(40)


def floor(value):
    """Redondea el valor hacia abajo a la casilla del tablero (tamaño 133)."""
    return ((value + 200) // 133) * 133 - 200


# Modificación 2: 'board' guarda las casillas ocupadas y quién las ocupó
# Modificación 3: 'over' indica si el juego ya terminó
state = {'player': 0, 'board': {}, 'over': False}
# Nombres de los jugadores: 0 = X, 1 = O
names = ['X', 'O']

# Modificación 2: coordenadas válidas de las 3 columnas/filas del tablero
cells = [-200, -67, 66]

# Modificación 3: las 8 combinaciones ganadoras (3 filas, 3 columnas, 2 diagonales)
wins = []
for c in cells:
    wins.append([(c, r) for r in cells])
    wins.append([(r, c) for r in cells])
wins.append([(cells[i], cells[i]) for i in range(3)])
wins.append([(cells[i], cells[2 - i]) for i in range(3)])


def winner():
    """Regresa el jugador ganador o None si nadie ha ganado."""
    board = state['board']
    for combo in wins:
        values = [board.get(cell) for cell in combo]
        if values[0] is not None and values.count(values[0]) == 3:
            return values[0]
    return None


def message(text):
    """Escribe un mensaje en el centro del tablero."""
    up()
    goto(0, -20)
    color('green')
    write(text, align='center', font=('Arial', 32, 'bold'))
    update()


# Funciones para dibujar a cada jugador
players = [drawx, drawo]


def tap(x, y):
    """Dibuja X u O en la casilla que se tocó."""
    # Modificación 3: si el juego ya terminó se ignoran los clics
    if state['over']:
        return

    x = floor(x)
    y = floor(y)

    # Modificación 2: se ignoran los clics fuera del tablero
    if x not in cells or y not in cells:
        return

    # Modificación 2: si la casilla ya está ocupada no se dibuja nada
    if (x, y) in state['board']:
        return

    player = state['player']
    state['board'][(x, y)] = player
    draw = players[player]
    draw(x, y)
    update()

    # Modificación 3: revisa si alguien ganó o si hubo empate
    ganador = winner()
    if ganador is not None:
        state['over'] = True
        message('Ganó ' + names[ganador])
        return
    if len(state['board']) == 9:
        state['over'] = True
        message('Empate')
        return

    # Cambia el turno al otro jugador
    state['player'] = not player


# Configuración de la ventana y arranque del juego
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
