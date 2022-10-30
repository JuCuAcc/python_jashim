

# Pygame has a Group class which makes working with a group of similar objects easier.
# A group is like a list, with some extra funcionality that's helpful when building games.

# Making and filling a group
# An object that will be placed in agroup must inherit from Sprite.

import pygame as pg 
from pygame.sprite import Sprite, Group

screen_dim = (1200, 800)
screen = pg.display.set_mode(screen_dim)

def Bullet(Sprite):
    #...
    def draw_bullet(self):
        #...
        pass
    def update(self):
        #...
        pass


bullets = Group()

new_bullet = Bullet()
bullets.add(new_bullet)

# Looping through the items in a group

# The sprites() method returns all the members of a group.

for bullet in bullets.sprites():
    bullet.draw_bullet()

# Calling update() on a group
# Calling update() on agroup automatically calls update() on each member of the group.
bullets.update()
# Removing an item from a group
bullets.remove()

# Detecting collisions
# You can detect when a single object collides with any member of a group.
# You can also detect when any member of one group collides with a member of another group.

# Collisions between a single object and a group
# The spritecollideany() function takes an object and a group, and
#  returns True if the object overlaps with any member of the group.

if pg.sprite.spritecollideany(ship, aliens): 
    ships_left -= 1

# Collisions between two groups
# The sprite.groupcollide() function takes two groups, and two booleans.
# The function returns a dictionary containing information about the members that have collided.
# The booleans tell Pygame whether to delete the members of either group that have collided.

collisions = pg.sprite.groupcollide(bullets, aliens, True, True)

score += len(collisions) * alien_point_value 

# Rendering text
# The font.render() function is used to create an image of the message,
#   and we get the rect object associated with the image.

msg = "Play again?"
msg_color = (100, 100, 100)
bg_color = (230, 230, 230)

f = pg.font.SysFont(None, 48)
msg_image = f.render(msg, True, msg_color, bg_color)
msg_image_rect =msg_image.get_rect()
msg_image_rect.center = screen_rect.center
screen.blit(msg_image, msg_image_rect)

