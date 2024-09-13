import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

fox = Actor("fox.png")
fox.pos = 100, 100
coin = Actor("coin.png")
coin.pos = 200, 200
    
def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("How many coins can you collect in 15s? ", color ="black", topleft=(5,5))
    screen.draw.text("Score " + str(score), color ="black", topleft=(23,23))
   
    if game_over == True:
        screen.fill("pink")
        screen.draw.text("Final score " + str(score), color ="black", topleft=(50,150), fontsize = 60) 

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))
    
def time_up():
    global game_over
    game_over = True

#update() built-in Pygame Zero function, runs 60 times a sec
def update():
    global score
    if score < 50:
        if keyboard.left or keyboard.A:
            fox.x = fox.x - 4
        elif keyboard.right or keyboard.D:
            fox.x = fox.x + 4
        elif keyboard.up or keyboard.W:
            fox.y = fox.y - 4
        elif keyboard.down or keyboard.S:
            fox.y = fox.y + 4
    elif score >= 50:
        if keyboard.left or keyboard.A:
            fox.x = fox.x - 6
        elif keyboard.right or keyboard.D:
            fox.x = fox.x + 6
        elif keyboard.up or keyboard.W:
            fox.y = fox.y - 6
        elif keyboard.down or keyboard.S:
            fox.y = fox.y + 6
            
    elif score >= 100:
        if keyboard.left or keyboard.A:
            fox.x = fox.x - 8
        elif keyboard.right or keyboard.D:
            fox.x = fox.x + 8
        elif keyboard.up or keyboard.W:
            fox.y = fox.y - 8
        elif keyboard.down or keyboard.S:
            fox.y = fox.y + 8
    
    # definning collidion (square) with fox    
    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 10
        place_coin()

#runs the function after 7 seconds from the game start
clock.schedule(time_up, 15.0)    
place_coin()
                
pgzrun.go()