"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    # Modificación 1: X roja, más gruesa, más pequeña y centrada en la casilla
    color('red')
    width(10)
    line(x + 30, y + 30, x + 103, y + 103)
    line(x + 30, y + 103, x + 103, y + 30)


def drawo(x, y):
    """Draw O player."""
    # Modificación 1: O azul, más gruesa, de radio 40 y centrada en la casilla
    color('blue')
    width(10)
    up()
    goto(x + 66.5, y + 26.5)
    down()
    circle(40)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
