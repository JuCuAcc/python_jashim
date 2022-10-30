
# http://pygame.org/
# http://pygame.org/docs/


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

    # Pygame rect objects

    screen_rect = screen.get_rect()
    screen_center = screen_rect.center

    # Individual  x and y values:
    screen_rect.left, screen_rect.right,
    screen_rect.top, screen_rect.bottom,
    screen_rect.centerx, screen_rect.centery,
    screen_rect.width, screen_rect.height

    # Tuples
    screen_rect.center
    screen_rect.size

    # The draw.rect() function takes a screen object, a color, and a rect.
    bullet_rect = pg.Rect(100, 100, 3, 15)
    color = (100, 100, 100)
    pg.draw.rect(screen, color, bullet_rect)

    # Loading an image 
    ship = pg.image.load('images/ship.png')
    # Getting the rect object from an image
    ship_rect = ship.get_rect()
    ship_rect.midbottom= screen_rect.midbottom

    # Draw ship to screen.
    screen.blit(ship, ship_rect)

    # Start main loop.
    while True: 
        # Start event loop.
        #for event in pg.event.get():
        #    if event.type == pg.QUIT:
        #        sys.exit()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN: 
                if event.key == pg.K_RIGHT:
                    ship_rect.x += 1 
                elif event.key == pg.K_LEFT:
                    ship_rect.x -= 1
                elif event.key == pg.K_SPACE:
                    ship.fire_bullet()
                elif event.key == pg.K_q:
                    sys.exit()

            if event.type == pg.KEYUP: 
                if event.key == pg.K_RIGHT:
                    ship.moving_right = False

        # Refresh screen.
        pg.display.flip()

run_game()

def blitme(self): 
    """Draw ship at current location."""
    self.screen.blit(self.image, self.rect)




