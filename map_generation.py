import pygame
import json
from grids.grid1 import *
from grids.grid2 import *
#from grids.grid3 import *

class Map:

    numgrille = 1

    TILESIZE = 40
    MAPWIDTH = 40
    MAPHEIGHT = 23
    DISPLAYWEIDTH = TILESIZE*MAPWIDTH
    DISPLAYHEIGHT = TILESIZE*MAPHEIGHT

    def __init__(self, player, screen):
            self.player = player
            self.screen = screen

    #def retrivegrid(self):


    def generatemap(self):
        if self.numgrille == 1:
            
            for row in range(self.MAPHEIGHT):
                for column in range(self.MAPWIDTH):
                    self.screen.blit(TEXTURES[GRID1[row][column]], (column*self.TILESIZE, row*self.TILESIZE))
            self.screen.blit(self.player.image,self.player.rect)
            pygame.display.update()
            
            if PASSAGE1_AREA.collidepoint(self.player.rect.x+20,self.player.rect.y):
                self.numgrille = 2 
                self.player.rect.x = 20
                self.player.rect.y = 400
        
        if self.numgrille == 2:

            #materialisation grille
            for row in range(self.MAPHEIGHT):
                for column in range(self.MAPWIDTH):
                    self.screen.blit(TEXTURES[GRID2[row][column]], (column*self.TILESIZE, row*self.TILESIZE))
            self.screen.blit(self.player.image,self.player.rect)
            pygame.display.update() 

            if PASSAGE2_AREA.collidepoint(self.player.rect.x+20,self.player.rect.y):
                self.numgrille = 1
                self.player.rect.x =1540
                self.player.rect.y = 400
        
