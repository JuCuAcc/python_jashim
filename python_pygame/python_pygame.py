
# pip install pygame
# https://youtu.be/Y4Jn0UCqY28
# Successfully installed pygame-2.1.2


# An empty game window
import sys 
import pygame as pg 

def run_game(): 
    # Initialize and set up screen.
    pg.init()
    #screen = pg.display.set_mode((1200, 800))
    screen_dim = (1200, 800)
    screen = pg.display.set_mode(screen_dim)
    bg_color = (230, 230, 230)
    screen.fill(bg_color)
    pg.display.set_caption("Alien Invasion")

    # Start main loop.
    while True: 
        # Start event loop.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        # Refresh screen.
        pg.display.flip()

run_game()



# Pygame rect objects

