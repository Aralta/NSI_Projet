import pygame
from animation import Player
from grid import *


pygame.init()


def deplacement (player):
    b=0
    a="0"
    tkey = pygame.key.get_pressed()
    for event in pygame.event.get():
    
        
        if tkey[pygame.K_ESCAPE]:
                    launched = False
                    pygame.quit()
    
        elif event.type == pygame.KEYDOWN:
            b = b+1
            
            if tkey [pygame.K_SPACE]:
                player.dash = 10
            if not tkey [pygame.K_SPACE]:
                player.dash = 0
                
            if b%5 == 0:
            
                player.moving = (player.moving + 1) % 2
                a = str(player.moving)
            
            if  tkey[pygame.K_RIGHT] and player.rect.x < DISPLAYWEIDTH-20:
                if COLLISION_AREA1.collidepoint(player.rect.x+20,player.rect.y):
                    player.rect.x -= 1
                else:
                    player.image = pygame.image.load ("Sprites/droite/" + a + ".png")
                    player.rect.x += player.velocity+ player.dash
                
            elif  tkey[pygame.K_DOWN]and player.rect.y <DISPLAYHEIGHT-20:
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