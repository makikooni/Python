import pgzrun
from random import randint

#setting up size of the game screen
WIDTH = 400
HEIGHT = 400

dots = []
lines = []

next_dot = 0 
number_of_dots = 10

for dot in range(0,number_of_dots):
    actor = Actor("dot.png")
    
    #at least 20 px from the edge of the screen
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)

def draw():
    screen.fill("grey")
    number = 1 
    for dot in dots:
        # +12 because...
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number = number + 1
    for line in lines:
        # screen.draw.line(x, y, (0,0,0))
        screen.draw.line(line[0], line[1], (100,0,0))
    
def on_mouse_down(pos):
    global next_dot
    global lines
    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot = next_dot + 1
    elif next_dot == number_of_dots -1:
        next_level()
        draw()  
    else:
        lines = []
        next_dot = 0
        
def next_level():
    global number_of_dots 
    number_of_dots += 5 
    global lines 
    lines = 0
    global next_dot 
    next_dot = 0
    

    
pgzrun.go()