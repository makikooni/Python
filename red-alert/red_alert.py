import pgzrun
import random

FONT_COLOR = (255, 255, 255) 

#constant vars in capital letters as a convention

#game window size:
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2 
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y) 

#number_of_levels:
FINAL_LEVEL = 10

START_SPEED = 10

#colors of stars that should not be clicked:
COLORS = ["green", "blue"]

game_over = False
game_complete = False
current_level =  1
stars = []
animations = []

def draw():
    global stars, current_level, game_over, game_complete
    screen.clear()
    #adding background image:
    screen.blit("space", (0, 0))
    if game_over:
        display_message("GAME OVER!", "Click space to try again.")
    elif game_complete:
        display_message("YOU WON!", "Well done. Try Again? Click space.")
    else:
        for star in stars:
            star.draw()
            
def update():
    global stars, game_complete, game_over, current_level
    if len(stars) == 0:
        stars = make_stars(current_level)
    if (game_complete or game_over) and keyboard.space:
        stars = []
        current_level = 1
        game_over = False
        game_complete = False
        
def make_stars(number_of_extra_stars):
    colors_to_create = get_colors_to_create(number_of_extra_stars)
    new_stars = create_stars(colors_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

def get_colors_to_create(number_of_extra_stars):
    colors_to_create = ["red"]
    for i in range(0, number_of_extra_stars):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create

def create_stars(colors_to_create):
    new_stars = []
    for color in colors_to_create:
        star = Actor(color + "-star")
        new_stars.append(star)
    return new_stars

def layout_stars(stars_to_layout):
    number_of_gaps = len(stars_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    #shuffle the position of stars along the x-axis
    random.shuffle(stars_to_layout)
    for index, star in enumerate(stars_to_layout):
        new_x_pos = (index + 1) * gap_size
        star.x = new_x_pos
        # modyfing code for two directions:
        if index % 2 != 0 and current_level >= 4:
            star.y = HEIGHT
        else:
            star.y = 0

def animate_stars(stars_to_animate):
    for star in stars_to_animate:
        duration = START_SPEED - current_level
        star.anchor = ("center", star.y)
        animation = animate(star, duration = duration, on_finished = handle_game_over, y = HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True
    
def on_mouse_down(pos):
    global stars, current_level
    for star in stars:
        if star.collidepoint(pos):
            if "red" in star.image:
                red_star_click()
            else:
                handle_game_over()
                
def red_star_click():
    global current_level, stars, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level = current_level + 1
        stars = []
        animations = []
        
def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text, fontsize=30, center=(CENTER_X, CENTER_Y + 30), color= FONT_COLOR)

def shuffle():
    global stars, current_level
    if stars and current_level >= 7:
        x_values = [star.x for star in stars] 
        random.shuffle(x_values)
        for index, star in enumerate(stars):
            new_x = x_values[index]
            animation = animate(star, duration=0.5, x=new_x) 
            animations.append(animation)

clock.schedule_interval(shuffle,1 )
pgzrun.go()