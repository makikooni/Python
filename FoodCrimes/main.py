
import pygame
from pygame.locals import *

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = pygame.image.load("FoodCrimes/assets/background.png")
    background = pygame.transform.scale(background, screen.get_size()) 

    #Add asset
    pc_image = pygame.image.load("FoodCrimes/assets/pc.png")
    pc_image = pygame.transform.scale(pc_image, (600, 600))  # Scale the PC image if needed
    pc_pos = pc_image.get_rect()  # Get the rectangle for positioning
    pc_pos.topleft = (350, 100) 
    

    # Display some text
    font = pygame.font.Font(None, 72)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    #textpos.centerx = background.get_rect().centerx
    textpos.topleft = (515, 270) 

    
    #This will be a list that will contain all the sprites we intend to use in our game.
    #all_sprites_list = pygame.sprite.Group()
    
        
    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        screen.blit(pc_image, pc_pos)
        screen.blit(text, textpos)
        pygame.display.flip()


if __name__ == '__main__': main()