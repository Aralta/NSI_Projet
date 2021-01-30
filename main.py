import pygame
from grids.grid1 import *
from grids.grid2 import *
from map_generation import *
from player import *

pygame.init()
player = Player()
player.rect.x = 500
player.rect.y = 500
map = Map(player, screen)
pygame.key.set_repeat(1,10)
true = True
launched = True



while launched:

    if game == 0:
        pygame.display.set_caption("Haku's ADVENTURES")
        screen = pygame.display.set_mode((1080,740))
        ecran()
        

    map.generatemap()
    deplacement (player,b,a)
    
    b = b + 1
    if b%5 == 0:
            
                player.moving = (player.moving + 1) % 2
                a = str(player.moving)
