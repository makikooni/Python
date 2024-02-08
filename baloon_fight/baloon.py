import pgzrun
from random import randint


#add music 
# add sound for clash


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
collision_cooldown = False

scores = []


def update_high_scores():
    global score, scores
    filename = r"baloon_fight/high-scores.txt" 
    scores = []
    with open(filename, "r") as file:
        line = file.readline()
        high_scores = line.split()
        for high_score in high_scores:
            if(score > int(high_score)):
                scores.append(str(score) + " ")
                score = int(high_score)
            else:
                scores.append(str(high_score) + " ")
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
    restart()
        
        
        
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
    global game_over, score, number_of_updates,lives, collision_cooldown
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
            while tree.x == house.x or tree.x == bird.x:
                tree.x = randint(800, 1600)
            score += 1
        
        # Not allowing touching the screen ends
        if balloon.top < 0 or balloon.bottom > 560:
            game_over = True
            update_high_scores()
        
        if not collision_cooldown:  # Only check collisions if not in cooldown
            if balloon.collidepoint(bird.x, bird.y) or balloon.collidepoint(house.x, house.y) or balloon.collidepoint(tree.x, tree.y):
                lives -= 1
                collision_cooldown = True  
                clock.schedule_unique(reset_collision_cooldown, 2)  # Schedule cooldown reset after 2 seconds
            if lives == 0:
                game_over = True
                update_high_scores()
                
            
def restart():
    global game_over, balloon, bird, house, tree, bird_up, up, score, number_of_updates, lives, collision_cooldown, scores
    if game_over and keyboard.space:
        balloon.pos = 400,300 #center of the screen
        bird.pos = randint(800,1600), randint(10,200) #x axis, y axis
        house.pos = randint(800,1600), 460
        tree.pos = randint(800, 1600), 450
        bird_up = True
        up = False
        game_over = False
        score = 0
        number_of_updates = 0
        lives = 3
        collision_cooldown = False
        scores = []

        
def reset_collision_cooldown():
    global collision_cooldown
    collision_cooldown = False 
                
                
pgzrun.go()