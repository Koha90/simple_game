from random import randint
from time import time

# This constants of screen scale
WIDTH = 400
HEIGHT = 400

# Global lists will store the dots and the lines
dots = []
lines = []

# Global variable starts at 0 and tells the game which dot should be clicked on next
next_dot = 0

for dot in range (0, 10):
    actor = Actor('dot')
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)

def draw():
    screen.fill('black')
    number = 1
    for dot in dots:
        screen.draw.text(str(number),
                         (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number = number + 1
    for line in lines:
        screen.draw.line(line[0], line[1], (225, 0, 0))

def update():
    pass

# define function for the click mouse on a dots
def on_mouse_down(pos):
    global next_dot
    global lines
    # connect the dots
    if dots[next_dot].collidepoint(pos):
        # this line checks if the player has already clicked on the first dot
        if next_dot:
            # this draws a line between the current dot and the previous one
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot = next_dot + 1
    else:
        lines = []
        next_dot = 0