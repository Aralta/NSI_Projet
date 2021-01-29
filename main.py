import pygame
from grids.grid1 import *
from grids.grid2 import *
from animation import Player
from animation import deplacement
from animation import *
from accueil import *

pygame.init()
player = Player()
player.rect.x = 500
player.rect.y = 500
pygame.key.set_repeat(1,10)
true = True
launched = True
numgrille = 1
game = 0


while launched:

    if game == 0:
        pygame.display.set_caption("Haku's ADVENTURES")
        screen = pygame.display.set_mode((1080,740))
        ecran()
        


    if game == 1: 
        pygame.display.set_caption("Haku's ADVENTURES")
        
        screen = pygame.display.set_mode((DISPLAYWEIDTH,DISPLAYHEIGHT))   
        #materialisation grille
        if numgrille == 1:
            for row in range(MAPHEIGHT):
                for column in range(MAPWIDTH):
                    screen.blit(TEXTURES[GRID1[row][column]], (column*TILESIZE, row*TILESIZE))
            screen.blit(player.image,player.rect)
            pygame.display.update()
            
            if PASSAGE1_AREA.collidepoint(player.rect.x+20,player.rect.y):
                numgrille = 2 
                player.rect.x = 20
                player.rect.y = 400
        
        if numgrille == 2:

            #materialisation grille
            for row in range(MAPHEIGHT):
                for column in range(MAPWIDTH):
                    screen.blit(TEXTURES[GRID2[row][column]], (column*TILESIZE, row*TILESIZE))
            screen.blit(player.image,player.rect)
            pygame.display.update() 

            if PASSAGE2_AREA.collidepoint(player.rect.x+20,player.rect.y):
                numgrille = 1
                player.rect.x =1540
                player.rect.y = 400
        
        deplacement (player,b,a)
        
        b = b + 1
        if b%5 == 0:
                
                    player.moving = (player.moving + 1) % 2
                    a = str(player.moving)

    print(game)