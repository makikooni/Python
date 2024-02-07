import pgzrun
from random import randint



#update scores so it only keeps top 5
#update score when obstacle passed.
#allow replay by space 
# space out obstacles
# repair 3 lives function


WIDTH = 800
HEIGHT = 600

balloon = Actor("balloon")
balloon.pos = 400,300 #center of the screen
bird = Actor("bird-up")
bird.pos = randint(800,1600), randint(10,200) #x axis, y axis
house = Actor("house")
house.pos = randint(800,1600), 460
tree = Actor("tree")
tree.pos = randint(800, 1600), 450


#Global variables:
bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0
lives = 3

scores = []


def update_high_scores():
    global score, scores
    filename = r"baloon_fight/high-scores.txt"
    scores = []
    score_updated = False
    with open(filename, "r") as file:
        line = file.readline()
        high_scores = line.split()
        for high_score in high_scores:
            if score > int(high_score):
                scores.append(str(score) + " ")
                score_updated = True
            else:
                scores.append(str(high_score) + " ")
    if not score_updated:
        scores.append(str(score) + " ")
    with open(filename, "w") as file:
        for high_score in scores:
            file.write(high_score)

def display_high_scores():
    global score, lives, game_over
    screen.draw.text("HIGH SCORES", (350, 150), color="black")
    y = 175
    position = 1
    for high_score in scores:
        screen.draw.text(str(position) + ". " + high_score, (350, y), color="black")
        y += 25
        position += 1
        
def draw():
    screen.blit("background", (0,0))
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text("Score: " + str(score), (700,5), color="black")
        screen.draw.text("Lives: " + str(lives), (700,25), color="black")
    else:
        display_high_scores()
        
        
        
def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True
        
def on_mouse_down():
    global up
    up = True
    balloon.y -= 50
    
    
def on_mouse_up():
    global up
    up = False
    
    
def update():
    global game_over, score, number_of_updates,lives 
    if not game_over:
        if not up:
            balloon.y += 1
            
        #if bird on the screen:
        if bird.x > 0:
            bird.x -= 4
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
            bird.x = randint(800, 1600)
            bird.y = randint(10, 200)
            # add a point for not touching an obstacle
            score += 1
            number_of_updates = 0
            
        if house.right > 0:
            house.x -= 2
        else:
            house.x = randint(800, 1600)
            score += 1
            
        if tree.right > 0:
            tree.x -= 2
        else:
            tree.x = randint(800, 1600)
            score += 1
        
        #not allowing touching the screen ends
        if balloon.top <0 or balloon.bottom > 560:
            lives -= 1
            if lives == 0:
                game_over = True
                update_high_scores()
            
            
        if balloon.collidepoint(bird.x, bird.y) or balloon.collidepoint(house.x, house.y) or balloon.collidepoint(tree.x, tree.y):
            lives -= 1
            if lives == 0:
                game_over = True 
                update_high_scores()
            
                
                
pgzrun.go()