import pygame
from grids.grid1 import *
from grids.grid2 import *
from map_generation import *
from player import *
from ecran_accueil import *


pygame.init()
pygame.display.set_caption("Haku's ADVENTURES")
screen = pygame.display.set_mode((DISPLAYWEIDTH,DISPLAYHEIGHT))
player = Player()
player.rect.x = 500
player.rect.y = 500
map = Map(player, screen)
pygame.key.set_repeat(1,10)
true = True
menu = True
game =False
launched = True
numgrille = 1

while launched:
    while menu :
                #position souris
        mouse_pos = pygame.mouse.get_pos()
                    
            #appuie sur une touche
        keypressed = pygame.key.get_pressed()      
    
        
        game_screen()
     
        pygame.display.update()  
        
        for event in pygame.event.get():   
            if event.type == pygame.MOUSEBUTTONDOWN:
                    menu = False
                    game =True
                    print("test")

    while game:
        
        map.generatemap()
        deplacement (player,b,a)
        
        b = b + 1
        if b%5 == 0:
                
                    player.moving = (player.moving + 1) % 2
                    a = str(player.moving)
