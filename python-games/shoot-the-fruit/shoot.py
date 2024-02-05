import pgzrun
from random import randint

#To-do: add a counter

#defining sprite
apple = Actor("apple.png")
orange = Actor("orange.png")
pineapple = Actor("pineapple.png")

def fruits():
    apple.draw()
    orange.draw()
    pineapple.draw()
    
#find out why theres no need to run the function 
def draw():
    screen.clear()
    fruits()
    


def place_fruits():
    #(0,0) == topleft
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)
    pineapple.x = randint(10, 800)
    pineapple.y = randint(10, 600)
   



def on_mouse_down(pos):
    #pos == position of the cursor
    if apple.collidepoint(pos):
        print("Good shot!")
        place_fruits()
    else:
        print("You missed")
        quit()
    
place_fruits()


pgzrun.go()