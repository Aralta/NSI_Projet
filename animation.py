#from pygame_functions import *
import pygame
pygame.init()
from grid1 import *

class Player:
    def __init__(self):
        self.image = pygame.image.load("Sprites/face/1.png")
        self.rect = self.image.get_rect()
        self.origin_image=self.image
        self.velocity =5
        self.moving = 0
        self.dash = 0
    
b=0
a="0"

def deplacement (player,b,a):
  
    
    
    tkey = pygame.key.get_pressed()
    for event in pygame.event.get():
        
        
        if tkey[pygame.K_ESCAPE]:
                    pygame.quit() 
                    launched = False
                    sys.exit()
                   
    
        elif event.type == pygame.KEYDOWN:
            
            
            if tkey [pygame.K_SPACE]:
                player.dash = 10
            if not tkey [pygame.K_SPACE]:
                player.dash = 0
            
            
                
            print(player.moving)
            print(b)
            print(a)
            if  tkey[pygame.K_RIGHT] and player.rect.x < DISPLAYWEIDTH-40:
                if COLLISION_AREA1.collidepoint(player.rect.x+20,player.rect.y):
                    player.rect.x -= 1
                else:
                    player.image = pygame.image.load ("Sprites/droite/" + a + ".png")
                    player.rect.x += player.velocity+ player.dash
                
            elif  tkey[pygame.K_DOWN]and player.rect.y <DISPLAYHEIGHT-40:
                if COLLISION_AREA1.collidepoint(player.rect.x,player.rect.y+20):
                    player.rect.y -= 1
                else:
                     player.rect.y += player.velocity + player.dash
                     player.image = pygame.image.load ("Sprites/face/" + a + ".png")
                    
            elif  tkey[pygame.K_LEFT]and player.rect.x >0 :
                if COLLISION_AREA1.collidepoint(player.rect.x,player.rect.y):
                    player.rect.x += 1
                else:
                    player.rect.x -= player.velocity+ player.dash
                    player.image = pygame.image.load ("Sprites/gauche/" + a + ".png")
                    
            elif  tkey[pygame.K_UP]and player.rect.y >0 :
                if COLLISION_AREA1.collidepoint(player.rect.x,player.rect.y):
                    player.rect.y += 1
                else:
                    player.rect.y -= player.velocity+ player.dash
                    player.image = pygame.image.load ("Sprites/fond/" + a + ".png")
           
  
            return b          