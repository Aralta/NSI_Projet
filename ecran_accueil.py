import pygame
from grids.grid1 import DISPLAYWEIDTH
from grids.grid1 import DISPLAYHEIGHT

pygame.init()
pygame.display.set_caption("Haku's ADVENTURES")
screen = pygame.display.set_mode((DISPLAYWEIDTH,DISPLAYHEIGHT))

#ecran d'accueil
def game_screen():
    
    #position souris
    mouse_pos = pygame.mouse.get_pos()
            
    #appuie sur une touche
    keypressed = pygame.key.get_pressed()
             
    #import image arriere plan
    background = pygame.image.load('Sprites/menu-ecran-accueil/background.png')
            
    #import sprite haku
    haku = pygame.image.load('Sprites/personnages/haku.png')
    haku_rect = haku.get_rect()
    haku_rect.x = DISPLAYWEIDTH/2.4
    haku_rect.y = DISPLAYHEIGHT/2.1
            
    #import sprite haku 2
    haku_hover = pygame.image.load('Sprites/personnages/haku 2.png')
    haku_hover_rect = haku_hover.get_rect()
    haku_hover_rect.x = DISPLAYWEIDTH/2.4
    haku_hover_rect.y = DISPLAYHEIGHT/2.1
            
    #import jouer
    play= pygame.image.load('Sprites/menu-ecran-accueil/clic.png')
    play_rect = play.get_rect()
    play_rect.x = DISPLAYWEIDTH/2.4
    play_rect.y = DISPLAYHEIGHT/1.9

    #jouer
    def haku_animation():
 
        if haku_rect.collidepoint(mouse_pos):
                
            screen.blit(haku_hover, haku_hover_rect)
            
            #animation haku 
            pygame.display.update()
            
        else:

            screen.blit(haku, haku_rect)
            

    #affichage arriere plan
    screen.blit(background, (0,0))
    screen.blit(play, play_rect)
    
    #bouton jouer
    haku_animation()


  

             
        
        

    
