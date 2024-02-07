import pgzrun
from random import randint

score = 0

#defining sprite
apple = Actor("apple.png")
orange = Actor("orange.png")
pineapple = Actor("pineapple.png")

def fruits():
    apple.draw()
    orange.draw()
    pineapple.draw()
    

def draw():
    screen.clear()
    fruits()
    screen.draw.text("Score " + str(score), color ="white", topleft=(23,23))

    


def place_fruits():
    #(0,0) == topleft
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)
    pineapple.x = randint(10, 800)
    pineapple.y = randint(10, 600)
   



def on_mouse_down(pos):
    global score
    #pos == position of the cursor
    if apple.collidepoint(pos):
        print("Good shot!")
        score = score + 1
        place_fruits()
    else:
        print("You missed")
        quit()
    
place_fruits()


pgzrun.go()