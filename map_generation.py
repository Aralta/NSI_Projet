from grids.grid1 import *
from grids.grid2 import *


def generatemap(numgrille,player,screen):
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
    
